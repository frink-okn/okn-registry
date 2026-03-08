"""MkDocs hook to load VoID stats and query listings into the Jinja2 template environment.

This makes `void_stats` and `kg_queries` available as globals in all templates,
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


def _parse_query_summary(rq_path: str) -> str:
    """Extract the summary from a .rq file's #+ header comments."""
    try:
        with open(rq_path) as f:
            for line in f:
                match = re.match(r"^#\+\s*summary:\s*(.+)$", line)
                if match:
                    return match.group(1).strip()
                # Stop looking after the header block ends
                if not line.startswith("#"):
                    break
    except OSError:
        pass
    return ""


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


def _read_query_text(rq_path: str) -> Markup:
    """Read the SPARQL query text from a .rq file, stripping the #+ header.

    Returns Pygments-highlighted HTML wrapped in Markup so Jinja2 won't escape it.
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
            code = "".join(lines).strip()
            return Markup(pygments_highlight(code, _sparql_lexer, _html_formatter))
    except OSError:
        return Markup("")


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

    # Build query file listings per KG shortname
    kg_queries = {}
    for rq in sorted(glob.glob("docs/registry/queries/**/*.rq", recursive=True)):
        parts = Path(rq).relative_to("docs/registry/queries").parts
        kg = parts[0]
        kg_queries.setdefault(kg, []).append({
            "name": Path(rq).stem,
            "summary": _parse_query_summary(rq),
            "path": rq,
            "text": _read_query_text(rq),
        })
    env.globals["kg_queries"] = kg_queries

    # Register custom filters
    env.filters["human_number"] = _human_number

    return env
