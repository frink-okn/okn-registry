"""Check that KG registry files have well-formed YAML frontmatter.

Each file must start with a `---` delimited YAML block that parses to a
non-empty mapping with no duplicate keys. This is a syntax check only; it does
not validate property names or values against a schema.

Usage:
    uv run scripts/check_registry.py [FILE ...]

With no FILE arguments, every docs/registry/kgs/*.md file is checked. Exits
with status 1 if any file fails. Under GitHub Actions, failures are also
emitted as error annotations so they show up on the pull request diff.
"""

import glob
import os
import sys

import frontmatter
import yaml

try:
    from yaml import CSafeLoader as _SafeLoader
except ImportError:
    from yaml import SafeLoader as _SafeLoader

DEFAULT_PATTERN = "docs/registry/kgs/*.md"
MERGE_TAG = "tag:yaml.org,2002:merge"


class UniqueKeyLoader(_SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys.

    PyYAML otherwise keeps the last value and silently drops the earlier ones.
    """

    def construct_mapping(self, node, deep=False):
        seen = set()
        for key_node, _ in node.value:
            if key_node.tag == MERGE_TAG:
                continue
            key = self.construct_object(key_node, deep=deep)
            try:
                duplicate = key in seen
            except TypeError:  # unhashable key; the base constructor reports it
                continue
            if duplicate:
                raise yaml.constructor.ConstructorError(
                    None, None, f"duplicate key {key!r}", key_node.start_mark
                )
            seen.add(key)
        return super().construct_mapping(node, deep=deep)


def check_file(path):
    """Return a list of (line, column, message) problems for one registry file.

    Line and column are 1-based positions in the file, or None when the problem
    has no position.
    """
    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except UnicodeDecodeError as e:
        return [(None, None, f"file is not valid UTF-8: {e}")]

    # Split the same way python-frontmatter does for the build scripts.
    boundary = frontmatter.YAMLHandler.FM_BOUNDARY
    opening = boundary.match(text)
    if not opening:
        return [(1, 1, "file must start with a '---' line opening the YAML frontmatter")]
    parts = boundary.split(text, 2)
    if len(parts) < 3:
        return [(1, 1, "YAML frontmatter is not closed by a '---' line")]
    fm = parts[1]
    # The frontmatter text starts with the remainder of the opening line.
    line_offset = text[: opening.end()].count("\n")

    try:
        data = yaml.load(fm, Loader=UniqueKeyLoader)
    except yaml.YAMLError as e:
        mark = getattr(e, "problem_mark", None) or getattr(e, "context_mark", None)
        if isinstance(e, yaml.MarkedYAMLError):
            message = ", ".join(p for p in (e.context, e.problem) if p)
        else:
            message = str(e)
        if mark is None:
            return [(None, None, f"invalid YAML frontmatter: {message}")]
        return [(line_offset + mark.line + 1, mark.column + 1, f"invalid YAML frontmatter: {message}")]

    if not isinstance(data, dict) or not data:
        return [(1, 1, "YAML frontmatter must be a non-empty mapping of keys to values")]
    return []


def _annotation_escape(value):
    return value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def main(argv):
    paths = argv or sorted(glob.glob(DEFAULT_PATTERN))
    if not paths:
        print(f"No files matched {DEFAULT_PATTERN}", file=sys.stderr)
        return 1

    in_actions = os.environ.get("GITHUB_ACTIONS") == "true"
    failed = 0
    for path in paths:
        problems = check_file(path)
        if problems:
            failed += 1
        for line, column, message in problems:
            location = path if line is None else f"{path}:{line}:{column}"
            print(f"{location}: {message}")
            if in_actions:
                position = "" if line is None else f",line={line},col={column}"
                print(f"::error file={path}{position}::{_annotation_escape(message)}")

    if failed:
        print(f"{failed} of {len(paths)} registry files have invalid frontmatter", file=sys.stderr)
        return 1
    print(f"Checked {len(paths)} registry files: frontmatter OK")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
