import json
import re
import sys
import os
import urllib.parse
import frontmatter


def _parse_query_header(rq_path: str) -> dict:
    """Extract the summary and tags from a .rq file's #+ header comments.

    Ripped from hooks/kg_page_data.py
    """
    summary = ""
    tags = []
    query_text = ""
    try:
        with open(rq_path) as f:
            in_tags = False
            query_text = f.read()
        for line in query_text.splitlines():
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
    return {"summary": summary, "tags": tags, "text": query_text}


def process_sparql_files(input_files, output_file):
    output = """
# Sample Query Library

| Title | Description |
| :---- | :---------- |
"""
    # Write the combined YAML to the output file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    for file in sorted(input_files):
        doc = _parse_query_header(file)
        taglist = ', '.join([tag for tag in doc['tags']])
        source_list = urllib.parse.quote(json.dumps(doc['tags']))
        query_text = urllib.parse.quote_plus(doc["text"])
        query_url = f'https://frink.apps.renci.org?sources={source_list}&amp;query={query_text}'
        output += f"| [{doc['summary']}]({query_url}) | {taglist} |\n"
    with open(output_file, "w") as f:
        f.write(output)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_query_list.py <output_file> <input_file1> [<input_file2> ...]")
        sys.exit(1)
    output_file = sys.argv[1]
    input_files = sys.argv[2:]
    process_sparql_files(input_files, output_file)
