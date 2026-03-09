"""MkDocs hook that populates the Jinja2 environment for KG pages.

Injects `void_stats`, `kg_queries`, and custom filters into all templates,
particularly the KG page template at material/overrides/kg.html.
"""

import glob
import re
from pathlib import Path

import yaml
from markupsafe import Markup
from pygments import highlight as pygments_highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import SparqlLexer

_sparql_lexer = SparqlLexer()
_html_formatter = HtmlFormatter(nowrap=True)

_MERMAID_BLOCK_RE = re.compile(r"```mermaid\s*\n(.*?)```", re.DOTALL)

# Patterns for unquoted edge labels that can confuse the Mermaid lexer
# (URLs with special characters like :, /, #, etc.)
_SOLID_EDGE_RE = re.compile(r'--((?!")[^\s>](?:(?!-->).)*?)-->')
_DOTTED_EDGE_RE = re.compile(r'-\.((?!")[^\s>](?:(?!\.\->).)*?)\.\->')


def _load_prefix_pairs() -> list[tuple[str, str]]:
    """Load prefix mappings from prefixes.yaml, sorted longest-URI-first."""
    try:
        with open("docs/registry/prefixes.yaml") as f:
            data = yaml.safe_load(f)
    except OSError:
        return []
    if not data:
        return []
    pairs = []
    for name, uri in data.items():
        pairs.append((uri, name))
        # Also match http variant for https URIs (tools may output either)
        if uri.startswith("https://"):
            pairs.append(("http://" + uri[8:], name))
    pairs.sort(key=lambda p: len(p[0]), reverse=True)
    return pairs


def _apply_prefixes(text: str, prefix_pairs: list[tuple[str, str]]) -> str:
    """Replace full URIs with prefixed forms (e.g. schema:name)."""
    for uri, name in prefix_pairs:
        text = text.replace(uri, name + ":")
    return text


def _quote_mermaid_edge_labels(mermaid: str) -> str:
    """Quote unquoted edge labels to prevent Mermaid syntax errors."""
    mermaid = _SOLID_EDGE_RE.sub(r'--"\1"-->', mermaid)
    mermaid = _DOTTED_EDGE_RE.sub(r'-."\1".->', mermaid)
    return mermaid


def _parse_query_header(rq_path: str) -> dict:
    """Extract the summary and tags from a .rq file's #+ header comments."""
    summary = ""
    tags = []
    try:
        with open(rq_path) as f:
            in_tags = False
            for line in f:
                if not line.startswith("#"):
                    break
                match = re.match(r"^#\+\s*summary:\s*(.+)$", line)
                if match:
                    # Strip optional surrounding quotes
                    summary = match.group(1).strip().strip('"').strip("'")
                    in_tags = False
                    continue
                if re.match(r"^#\+\s*tags:\s*$", line):
                    in_tags = True
                    continue
                if in_tags:
                    tag_match = re.match(r"^#\+\s*-\s*(.+)$", line)
                    if tag_match:
                        tags.append(tag_match.group(1).strip())
                    else:
                        in_tags = False
    except OSError:
        pass
    return {"summary": summary, "tags": tags}


def _human_number(value):
    """Format a large number for display: 12345678 -> '12.3M'."""
    try:
        n = int(value)
    except (TypeError, ValueError):
        return str(value)
    if n >= 1_000_000_000:
        return f"{n / 1_000_000_000:.1f}B"
    if n >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n / 1_000:.1f}K"
    return str(n)


def _read_query_text(rq_path: str) -> tuple[str, Markup]:
    """Read the SPARQL query text from a .rq file, stripping the #+ header.

    Returns (raw_text, highlighted_html).
    """
    try:
        with open(rq_path) as f:
            lines = []
            past_header = False
            for line in f:
                if not past_header and line.startswith("#+"):
                    continue
                past_header = True
                lines.append(line)
            raw = "".join(lines).strip()
            highlighted = Markup(pygments_highlight(raw, _sparql_lexer, _html_formatter))
            return raw, highlighted
    except OSError:
        return "", Markup("")


def _extract_mermaid(md_path: str, prefix_pairs: list[tuple[str, str]]) -> str:
    """Extract the mermaid code block from a generated .md file."""
    try:
        content = Path(md_path).read_text()
    except OSError:
        return ""
    match = _MERMAID_BLOCK_RE.search(content)
    if not match:
        return ""
    mermaid = match.group(1).strip()
    mermaid = _apply_prefixes(mermaid, prefix_pairs)
    mermaid = _quote_mermaid_edge_labels(mermaid)
    return mermaid


def on_env(env, config, files, **kwargs):
    """Inject VoID stats and query listings into the Jinja2 environment."""

    # Load VoID stats
    void_stats = {}
    for f in glob.glob("docs/registry/void/*.yaml"):
        shortname = Path(f).stem
        with open(f) as fh:
            data = yaml.safe_load(fh)
            if data:
                void_stats[shortname] = data
    env.globals["void_stats"] = void_stats

    # Load prefix mappings for compact URIs in mermaid diagrams
    prefix_pairs = _load_prefix_pairs()

    # Build query file listings per KG shortname
    kg_queries = {}
    for rq in sorted(glob.glob("docs/registry/queries/**/*.rq", recursive=True)):
        parts = Path(rq).relative_to("docs/registry/queries").parts
        dir_kg = parts[0]
        header = _parse_query_header(rq)
        raw_text, highlighted = _read_query_text(rq)

        # Look for a .md file generated by sparql-examples-utils in build/
        rel = str(Path(rq).relative_to("docs/registry/queries"))
        md_path = f"build/query-diagrams/{rel[:-3]}.md"
        mermaid = _extract_mermaid(md_path, prefix_pairs)

        entry = {
            "name": Path(rq).stem,
            "summary": header["summary"],
            "tags": header["tags"],
            "path": rq,
            "raw_text": raw_text,
            "text": highlighted,
            "mermaid": mermaid,
        }

        # Index by tags if present, otherwise by directory name
        target_kgs = header["tags"] if header["tags"] else [dir_kg]
        for kg in target_kgs:
            kg_queries.setdefault(kg, []).append(entry)
    env.globals["kg_queries"] = kg_queries

    # Register custom filters
    env.filters["human_number"] = _human_number

    return env
