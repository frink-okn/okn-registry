import glob
import os

all_kg_files = glob.glob("docs/registry/kgs/*.md")
all_query_rq_files = glob.glob("docs/registry/queries/**/*.rq", recursive=True)
all_query_ttl_files = [
    f"build/query-diagrams/{path.removeprefix('docs/registry/queries/')[:-3]}.ttl"
    for path in all_query_rq_files
]
all_query_md_files = [
    f"build/query-diagrams/{path.removeprefix('docs/registry/queries/')[:-3]}.md"
    for path in all_query_rq_files
]

SPARQL_EXAMPLES_UTILS_VERSION = "2.0.23"
SPARQL_EXAMPLES_UTILS_JAR = f"tools/sparql-examples-utils-{SPARQL_EXAMPLES_UTILS_VERSION}-uber.jar"
SPARQL_EXAMPLES_UTILS_URL = (
    "https://github.com/sib-swiss/sparql-examples-utils/releases/download/"
    f"v{SPARQL_EXAMPLES_UTILS_VERSION}/"
    f"sparql-examples-utils-{SPARQL_EXAMPLES_UTILS_VERSION}-uber.jar"
)
SPARQL_EXAMPLES_BASE_IRI = os.environ.get(
    "SPARQL_EXAMPLES_BASE_IRI",
    "https://example.org/sparql-examples/",
)


rule download_sparql_examples_utils:
    output:
        SPARQL_EXAMPLES_UTILS_JAR
    params:
        url=SPARQL_EXAMPLES_UTILS_URL
    shell:
        """
        mkdir -p $(dirname {output})
        curl -L --fail --silent --show-error -o {output} {params.url}
        """


rule rq_to_ttl:
    input:
        rq="docs/registry/queries/{query_path}.rq",
        jar=SPARQL_EXAMPLES_UTILS_JAR
    output:
        ttl="build/query-diagrams/{query_path}.ttl"
    params:
        base_iri=SPARQL_EXAMPLES_BASE_IRI
    shell:
        """
        mkdir -p $(dirname {output.ttl})
        tmpdir=$(mktemp -d)
        trap 'rm -rf "$tmpdir"' EXIT
        cp {input.rq} "$tmpdir/"
        java -jar {input.jar} import-rq -i "$tmpdir" -b {params.base_iri}
        python3 scripts/dedupe_sparql_prefixes.py "$tmpdir/$(basename {output.ttl})"
        cp "$tmpdir/$(basename {output.ttl})" {output.ttl}
        """


rule ttl_to_markdown:
    input:
        rq="docs/registry/queries/{query_path}.rq",
        ttl="build/query-diagrams/{query_path}.ttl",
        jar=SPARQL_EXAMPLES_UTILS_JAR
    output:
        md="build/query-diagrams/{query_path}.md"
    shell:
        """
        mkdir -p $(dirname {output.md})
        tmpdir=$(mktemp -d)
        trap 'rm -rf "$tmpdir"' EXIT
        project_dir=$(dirname {wildcards.query_path})
        mkdir -p "$tmpdir/$project_dir"
        cp {input.rq} "$tmpdir/$project_dir/"
        cp {input.ttl} "$tmpdir/$project_dir/"
        java -jar {input.jar} convert -i "$tmpdir" -m || echo "WARNING: diagram generation failed for {wildcards.query_path}" >&2
        if [ -f "$tmpdir/$project_dir/$(basename {output.md})" ]; then
            cp "$tmpdir/$project_dir/$(basename {output.md})" {output.md}
        else
            touch {output.md}
        fi
        """


rule build_query_docs:
    input:
        all_query_ttl_files,
        all_query_md_files


rule fetch_void_stats:
    input:
        registry="docs/registry/kgs.yaml",
        script="scripts/fetch_void_stats.py",
        uv_project="pyproject.toml"
    output:
        directory("docs/registry/void")
    shell:
        """uv run {input.script} {input.registry} {output}"""

rule compile_registry:
    input:
        files=all_kg_files,
        script="scripts/combine_registry.py",
        uv_project="pyproject.toml"
    output:
        "docs/registry/kgs.yaml"
    shell:
        """uv run {input.script} {output} {input.files}"""

rule generate_registry_index:
    input:
        files=all_kg_files,
        script="scripts/generate_registry_index.py",
        uv_project="pyproject.toml"
    output:
        "docs/registry/index.md"
    shell:
        """uv run {input.script} {output} {input.files}"""
