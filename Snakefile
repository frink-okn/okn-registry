import glob

all_kg_files = glob.glob("docs/registry/kgs/*.md")

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
