"""Fetch VoID statistics for all registered KGs from the central okn-void endpoint.

Usage:
    python fetch_void_stats.py <registry_yaml> <output_dir>

Queries https://frink.apps.renci.org/okn-void/sparql for VoID metadata
and writes a YAML file per KG into <output_dir>/<shortname>.yaml.
"""

import sys
import json
import os
from datetime import date, timezone, datetime
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import URLError

import yaml

VOID_ENDPOINT = "https://frink.apps.renci.org/okn-void/sparql"
DATASET_BASE = "https://purl.org/okn/frink/kg/"
PREFIXES_FILE = Path(__file__).resolve().parent.parent / "docs" / "registry" / "prefixes.yaml"
TIMEOUT = 30  # seconds per query

# Loaded at runtime from prefixes.yaml; maps namespace URI -> "prefix:"
PREFIXES: dict[str, str] = {}


def load_prefixes():
    """Load prefix mappings from the shared prefixes.yaml file."""
    global PREFIXES
    if not PREFIXES_FILE.exists():
        print(f"  Warning: {PREFIXES_FILE} not found, using no prefixes", file=sys.stderr)
        return
    with open(PREFIXES_FILE) as f:
        raw = yaml.safe_load(f) or {}
    # Invert: the YAML is {prefix: namespace}, we need {namespace: "prefix:"}
    # Sort by namespace length descending so longer matches win
    PREFIXES = dict(
        sorted(
            ((ns, f"{prefix}:") for prefix, ns in raw.items()),
            key=lambda item: len(item[0]),
            reverse=True,
        )
    )


def compact_uri(uri: str) -> str:
    """Shorten a URI using prefixes from prefixes.yaml."""
    for namespace, prefix in PREFIXES.items():
        if uri.startswith(namespace):
            return prefix + uri[len(namespace):]
    # Fall back to local name after last / or #
    for sep in ("#", "/"):
        if sep in uri:
            return uri.rsplit(sep, 1)[1]
    return uri


def sparql_query(query: str) -> list[dict]:
    """Execute a SPARQL SELECT query and return the bindings list."""
    params = urlencode({"query": query})
    url = f"{VOID_ENDPOINT}?{params}"
    req = Request(url, headers={"Accept": "application/sparql-results+json"})
    try:
        with urlopen(req, timeout=TIMEOUT) as resp:
            data = json.loads(resp.read())
            return data["results"]["bindings"]
    except (URLError, TimeoutError, json.JSONDecodeError, KeyError) as e:
        print(f"  SPARQL query failed: {e}", file=sys.stderr)
        return []


def get_value(binding: dict, var: str, as_int: bool = False):
    """Extract a value from a SPARQL binding, optionally as int."""
    if var not in binding:
        return None
    val = binding[var]["value"]
    if as_int:
        try:
            return int(val)
        except (ValueError, TypeError):
            return None
    return val


def fetch_summary_stats(shortnames: list[str]) -> dict[str, dict]:
    """Fetch top-level VoID stats for all KGs in a single query."""
    values = " ".join(f"<{DATASET_BASE}{s}>" for s in shortnames)
    query = f"""
    PREFIX void: <http://rdfs.org/ns/void#>
    PREFIX dct: <http://purl.org/dc/terms/>
    SELECT ?dataset ?triples ?subjects ?objects ?properties ?issued WHERE {{
      VALUES ?dataset {{ {values} }}
      ?dataset a void:Dataset .
      OPTIONAL {{ ?dataset void:triples ?triples }}
      OPTIONAL {{ ?dataset void:distinctSubjects ?subjects }}
      OPTIONAL {{ ?dataset void:distinctObjects ?objects }}
      OPTIONAL {{ ?dataset void:properties ?properties }}
      OPTIONAL {{ ?dataset dct:issued ?issued }}
    }}
    """
    bindings = sparql_query(query)
    results = {}
    for b in bindings:
        uri = get_value(b, "dataset")
        if not uri:
            continue
        shortname = uri.rsplit("/", 1)[1]
        results[shortname] = {
            "triples": get_value(b, "triples", as_int=True),
            "distinct_subjects": get_value(b, "subjects", as_int=True),
            "distinct_objects": get_value(b, "objects", as_int=True),
            "properties": get_value(b, "properties", as_int=True),
            "issued": get_value(b, "issued"),
        }
    return results


def fetch_class_partitions(shortname: str) -> list[dict]:
    """Fetch class partition data for a single KG."""
    query = f"""
    PREFIX void: <http://rdfs.org/ns/void#>
    SELECT ?class ?entityCount WHERE {{
      <{DATASET_BASE}{shortname}> void:classPartition ?cp .
      ?cp void:class ?class .
      OPTIONAL {{ ?cp void:entities ?entityCount }}
    }} ORDER BY DESC(?entityCount)
    """
    bindings = sparql_query(query)
    results = []
    for b in bindings:
        uri = get_value(b, "class")
        if uri:
            results.append({
                "uri": uri,
                "label": compact_uri(uri),
                "count": get_value(b, "entityCount", as_int=True),
            })
    return results


def fetch_property_partitions(shortname: str) -> list[dict]:
    """Fetch property partition data for a single KG."""
    query = f"""
    PREFIX void: <http://rdfs.org/ns/void#>
    SELECT ?property ?tripleCount WHERE {{
      <{DATASET_BASE}{shortname}> void:propertyPartition ?pp .
      ?pp void:property ?property .
      OPTIONAL {{ ?pp void:triples ?tripleCount }}
    }} ORDER BY DESC(?tripleCount)
    """
    bindings = sparql_query(query)
    results = []
    for b in bindings:
        uri = get_value(b, "property")
        if uri:
            results.append({
                "uri": uri,
                "label": compact_uri(uri),
                "count": get_value(b, "tripleCount", as_int=True),
            })
    return results


def load_shortnames(registry_yaml: str) -> list[str]:
    """Load all shortnames from the compiled registry YAML."""
    with open(registry_yaml) as f:
        data = yaml.safe_load(f)
    return [kg["shortname"] for kg in data.get("kgs", []) if "shortname" in kg]


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "Usage: fetch_void_stats.py <registry_yaml> <output_dir>",
            file=sys.stderr,
        )
        return 2

    registry_yaml = sys.argv[1]
    output_dir = Path(sys.argv[2])
    output_dir.mkdir(parents=True, exist_ok=True)

    load_prefixes()

    shortnames = load_shortnames(registry_yaml)
    print(f"Fetching VoID stats for {len(shortnames)} KGs...")

    # Batch fetch summary stats
    summary = fetch_summary_stats(shortnames)
    today = date.today().isoformat()

    for shortname in shortnames:
        stats = summary.get(shortname)
        if not stats:
            print(f"  {shortname}: no VoID data found, skipping")
            continue

        print(f"  {shortname}: {stats.get('triples', '?')} triples")

        # Fetch partitions for this KG
        classes = fetch_class_partitions(shortname)
        properties = fetch_property_partitions(shortname)

        stats["classes"] = len(classes)
        stats["last_checked"] = today
        # issued will be None until dct:issued triples are added
        if stats.get("issued") is None:
            stats.pop("issued", None)
        stats["class_partitions"] = classes
        stats["property_partitions"] = properties

        out_path = output_dir / f"{shortname}.yaml"
        with open(out_path, "w") as f:
            yaml.dump(stats, f, sort_keys=False, default_flow_style=False)

    # Remove void YAML files for KGs no longer in the registry
    for existing in output_dir.glob("*.yaml"):
        if existing.stem not in shortnames:
            print(f"  Removing stale {existing.name}")
            existing.unlink()

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
