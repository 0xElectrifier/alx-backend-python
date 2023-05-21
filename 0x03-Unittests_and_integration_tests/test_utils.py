#!/usr/bin/env python3
"""Parameterize a unit test"""
from parameterized import parameterized
from typing import ( Dict, Tuple )
from unittest import TestCase


class TestAccessNestedMap(TestCase):
    """
    Subclass of unittest.TestCase for testing the @utils.access_nested_map
    function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple, expected: int):
        """Tests the function"""
        access_nested_map = __import__("utils").access_nested_map
        self.assertEqual(access_nested_map(nested_map, path), expected)
