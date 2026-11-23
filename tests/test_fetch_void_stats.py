import unittest
from unittest.mock import patch

from scripts import fetch_void_stats


class FetchVoidStatsTests(unittest.TestCase):
    def test_sort_partitions_orders_ties_by_uri(self):
        partitions = [
            {"uri": "https://example.org/z", "label": "z", "count": 2},
            {"uri": "https://example.org/a", "label": "a", "count": 2},
            {"uri": "https://example.org/b", "label": "b", "count": None},
            {"uri": "https://example.org/c", "label": "c", "count": 5},
        ]

        self.assertEqual(
            fetch_void_stats.sort_partitions(partitions),
            [
                {"uri": "https://example.org/c", "label": "c", "count": 5},
                {"uri": "https://example.org/a", "label": "a", "count": 2},
                {"uri": "https://example.org/z", "label": "z", "count": 2},
                {"uri": "https://example.org/b", "label": "b", "count": None},
            ],
        )

    @patch("scripts.fetch_void_stats.compact_uri", side_effect=lambda uri: uri.rsplit("/", 1)[1])
    @patch("scripts.fetch_void_stats.sparql_query")
    def test_fetch_all_class_partitions_sorts_results_deterministically(
        self,
        mock_sparql_query,
        _mock_compact_uri,
    ):
        mock_sparql_query.return_value = [
            {
                "dataset": {"value": "https://purl.org/okn/frink/kg/demo"},
                "class": {"value": "https://example.org/z"},
                "entityCount": {"value": "2"},
            },
            {
                "dataset": {"value": "https://purl.org/okn/frink/kg/demo"},
                "class": {"value": "https://example.org/a"},
                "entityCount": {"value": "2"},
            },
            {
                "dataset": {"value": "https://purl.org/okn/frink/kg/demo"},
                "class": {"value": "https://example.org/c"},
                "entityCount": {"value": "5"},
            },
        ]

        self.assertEqual(
            fetch_void_stats.fetch_all_class_partitions("https://example.org/sparql", ["demo"]),
            {
                "demo": [
                    {"uri": "https://example.org/c", "label": "c", "count": 5},
                    {"uri": "https://example.org/a", "label": "a", "count": 2},
                    {"uri": "https://example.org/z", "label": "z", "count": 2},
                ]
            },
        )


if __name__ == "__main__":
    unittest.main()
