"""Fetch VoID statistics for all registered KGs from the central okn-void endpoint.

Usage:
    python fetch_void_stats.py <registry_yaml> <output_dir>

Queries the okn-void SPARQL endpoint listed in the registry for VoID metadata
and writes a YAML file per KG into <output_dir>/<shortname>.yaml.
"""

import sys
import json
from datetime import date
from time import sleep
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import URLError

import yaml

DATASET_BASE = "https://purl.org/okn/frink/kg/"
PREFIXES_FILE = Path(__file__).resolve().parent.parent / "docs" / "registry" / "prefixes.yaml"
TIMEOUT = 30  # seconds per query
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds, multiplied by the attempt number

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


def sparql_query(endpoint: str, query: str, label: str) -> list[dict]:
    """Execute a SPARQL SELECT query and return the bindings list."""
    params = urlencode({"query": query})
    url = f"{endpoint}?{params}"
    req = Request(url, headers={"Accept": "application/sparql-results+json"})
    last_error: Exception | None = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with urlopen(req, timeout=TIMEOUT) as resp:
                data = json.loads(resp.read())
                return data["results"]["bindings"]
        except (URLError, TimeoutError, json.JSONDecodeError, KeyError) as e:
            last_error = e
            if attempt == MAX_RETRIES:
                break
            delay = RETRY_DELAY * attempt
            print(
                f"  SPARQL query failed for {label} "
                f"(attempt {attempt}/{MAX_RETRIES}): {e}; retrying in {delay}s",
                file=sys.stderr,
            )
            sleep(delay)
    raise RuntimeError(
        f"SPARQL query failed for {label} after {MAX_RETRIES} attempts: {last_error}"
    )


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


def sort_partitions(partitions: list[dict]) -> list[dict]:
    """Sort partition rows deterministically."""
    return sorted(
        partitions,
        key=lambda item: (
            item.get("count") is None,
            -(item.get("count") or 0),
            item["uri"],
        ),
    )


def fetch_summary_stats(endpoint: str, shortnames: list[str]) -> dict[str, dict]:
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
    bindings = sparql_query(endpoint, query, "summary stats")
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


def fetch_all_class_partitions(endpoint: str, shortnames: list[str]) -> dict[str, list[dict]]:
    """Fetch class partition data for all KGs in a single query."""
    values = " ".join(f"<{DATASET_BASE}{s}>" for s in shortnames)
    query = f"""
    PREFIX void: <http://rdfs.org/ns/void#>
    SELECT ?dataset ?class ?entityCount WHERE {{
      VALUES ?dataset {{ {values} }}
      ?dataset void:classPartition ?cp .
      ?cp void:class ?class .
      OPTIONAL {{ ?cp void:entities ?entityCount }}
    }} ORDER BY ?dataset DESC(?entityCount)
    """
    bindings = sparql_query(endpoint, query, "class partitions")
    results: dict[str, list[dict]] = {}
    for b in bindings:
        ds = get_value(b, "dataset")
        uri = get_value(b, "class")
        if not ds or not uri:
            continue
        shortname = ds.rsplit("/", 1)[1]
        results.setdefault(shortname, []).append({
            "uri": uri,
            "label": compact_uri(uri),
            "count": get_value(b, "entityCount", as_int=True),
        })
    return {
        shortname: sort_partitions(partitions)
        for shortname, partitions in results.items()
    }


def fetch_all_property_partitions(endpoint: str, shortnames: list[str]) -> dict[str, list[dict]]:
    """Fetch property partition data for all KGs in a single query."""
    values = " ".join(f"<{DATASET_BASE}{s}>" for s in shortnames)
    query = f"""
    PREFIX void: <http://rdfs.org/ns/void#>
    SELECT ?dataset ?property ?tripleCount WHERE {{
      VALUES ?dataset {{ {values} }}
      ?dataset void:propertyPartition ?pp .
      ?pp void:property ?property .
      OPTIONAL {{ ?pp void:triples ?tripleCount }}
    }} ORDER BY ?dataset DESC(?tripleCount)
    """
    bindings = sparql_query(endpoint, query, "property partitions")
    results: dict[str, list[dict]] = {}
    for b in bindings:
        ds = get_value(b, "dataset")
        uri = get_value(b, "property")
        if not ds or not uri:
            continue
        shortname = ds.rsplit("/", 1)[1]
        results.setdefault(shortname, []).append({
            "uri": uri,
            "label": compact_uri(uri),
            "count": get_value(b, "tripleCount", as_int=True),
        })
    return {
        shortname: sort_partitions(partitions)
        for shortname, partitions in results.items()
    }


def load_registry(registry_yaml: str) -> list[dict]:
    """Load KG entries from the compiled registry YAML."""
    with open(registry_yaml) as f:
        data = yaml.safe_load(f) or {}
    return data.get("kgs", [])


def load_shortnames(kgs: list[dict]) -> list[str]:
    """Load all shortnames from the registry entries."""
    return [kg["shortname"] for kg in kgs if "shortname" in kg]


def load_void_endpoint(kgs: list[dict]) -> str:
    """Load the okn-void SPARQL endpoint from the registry entries."""
    for kg in kgs:
        if kg.get("shortname") != "okn-void":
            continue
        endpoint = kg.get("sparql")
        if not endpoint:
            raise ValueError("Registry entry for okn-void has no sparql field")
        return endpoint
    raise ValueError("No okn-void entry found in registry")


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

    kgs = load_registry(registry_yaml)
    shortnames = load_shortnames(kgs)
    void_endpoint = load_void_endpoint(kgs)
    print(f"Fetching VoID stats for {len(shortnames)} KGs from {void_endpoint}...")

    # Batch fetch all stats
    summary = fetch_summary_stats(void_endpoint, shortnames)
    all_classes = fetch_all_class_partitions(void_endpoint, shortnames)
    all_properties = fetch_all_property_partitions(void_endpoint, shortnames)
    if summary and not all_classes and not all_properties:
        raise RuntimeError(
            "No VoID class or property partitions were fetched; "
            "refusing to overwrite existing partition data with empty results"
        )
    today = date.today().isoformat()

    for shortname in shortnames:
        stats = summary.get(shortname)
        if not stats:
            print(f"  {shortname}: no VoID data found, skipping")
            continue

        print(f"  {shortname}: {stats.get('triples', '?')} triples")

        classes = all_classes.get(shortname, [])
        properties = all_properties.get(shortname, [])

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
