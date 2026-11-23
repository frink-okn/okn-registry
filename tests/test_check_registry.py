import contextlib
import io
import os
import tempfile
import unittest
from unittest.mock import patch

from scripts import check_registry

VALID = """---
template: overrides/kg.html
shortname: example
title: Example KG
description: "An example: with a colon"
contacts:
  - email: someone@example.org
    label: Someone
---
Narrative text.
"""


class CheckRegistryTests(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmpdir.cleanup)

    def write(self, text, name="example.md"):
        path = os.path.join(self.tmpdir.name, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return path

    def test_valid_file_has_no_problems(self):
        self.assertEqual(check_registry.check_file(self.write(VALID)), [])

    def test_unquoted_colon_reports_file_line(self):
        text = VALID.replace('"An example: with a colon"', "An example: with a colon")
        [(line, column, message)] = check_registry.check_file(self.write(text))
        self.assertEqual((line, column), (5, 24))
        self.assertIn("mapping values are not allowed", message)

    def test_duplicate_key_is_rejected(self):
        text = VALID.replace("title: Example KG\n", "title: Example KG\ntitle: Again\n")
        [(line, column, message)] = check_registry.check_file(self.write(text))
        self.assertEqual((line, column), (5, 1))
        self.assertIn("duplicate key 'title'", message)

    def test_duplicate_nested_key_is_rejected(self):
        text = VALID.replace("    label: Someone\n", "    label: Someone\n    email: other@example.org\n")
        [(line, _, message)] = check_registry.check_file(self.write(text))
        self.assertEqual(line, 9)
        self.assertIn("duplicate key 'email'", message)

    def test_missing_frontmatter_is_rejected(self):
        [(_, _, message)] = check_registry.check_file(self.write("Just text.\n"))
        self.assertIn("must start with a '---' line", message)

    def test_unclosed_frontmatter_is_rejected(self):
        [(_, _, message)] = check_registry.check_file(self.write("---\nshortname: example\n"))
        self.assertIn("not closed", message)

    def test_non_mapping_frontmatter_is_rejected(self):
        [(_, _, message)] = check_registry.check_file(self.write("---\n- a\n- b\n---\nText.\n"))
        self.assertIn("non-empty mapping", message)

    def test_main_reports_failures_and_exit_status(self):
        good = self.write(VALID, "good.md")
        bad = self.write(VALID.replace("title: Example KG\n", "title: Example KG\ntitle: Again\n"), "bad.md")
        out = io.StringIO()
        with patch.dict(os.environ, {"GITHUB_ACTIONS": "true"}), contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            status = check_registry.main([good, bad])
        self.assertEqual(status, 1)
        self.assertIn(f"{bad}:5:1: invalid YAML frontmatter: duplicate key 'title'", out.getvalue())
        self.assertIn(f"::error file={bad},line=5,col=1::", out.getvalue())
        self.assertNotIn(good, out.getvalue())

        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(check_registry.main([good]), 0)


if __name__ == "__main__":
    unittest.main()
