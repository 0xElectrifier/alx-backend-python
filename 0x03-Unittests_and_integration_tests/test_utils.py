#!/usr/bin/env python3
"""Parameterize a unit test"""
from parameterized import parameterized
from typing import ( Dict, Tuple )
from unittest import TestCase

access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(TestCase):
    """
    Subclass of unittest.TestCase for testing the @utils.access_nested_map
    function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple, expected: int):
        """
        Checks that @utils.access_nested_map function returns expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Tests @utils.access_nested_map function raises a KeyError when a
        key isn't found.
        """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)
