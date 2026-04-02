import re
import sys
from pathlib import Path


def dedupe_prefixes_in_query_block(block: str) -> str:
    prefix_pattern = re.compile(
        r"^\s*PREFIX\s+([A-Za-z][\w\-]*)\s*:\s*(<[^>]+>|\S+)\s*$",
        flags=re.IGNORECASE,
    )
    seen_prefixes = set()
    output_lines = []

    for line in block.splitlines():
        prefix_match = prefix_pattern.match(line)
        if prefix_match:
            prefix_label = prefix_match.group(1)
            prefix = prefix_label.lower()
            namespace = prefix_match.group(2)
            if namespace.startswith("<") and namespace.endswith(">"):
                normalized_namespace = namespace
            else:
                normalized_namespace = f"<{namespace}>"
            if prefix in seen_prefixes:
                continue
            seen_prefixes.add(prefix)
            output_lines.append(f"PREFIX {prefix_label}: {normalized_namespace}")
            continue
        output_lines.append(line)

    return "\n".join(output_lines)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: dedupe_sparql_prefixes.py <ttl-file>", file=sys.stderr)
        return 2

    ttl_path = Path(sys.argv[1])
    content = ttl_path.read_text()

    triple_quote = '"' * 3
    block_pattern = re.compile(r"\"\"\"(.*?)\"\"\"", flags=re.DOTALL)

    def replacer(match: re.Match[str]) -> str:
        body = match.group(1)
        return triple_quote + dedupe_prefixes_in_query_block(body) + triple_quote

    updated = block_pattern.sub(replacer, content)
    ttl_path.write_text(updated)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
