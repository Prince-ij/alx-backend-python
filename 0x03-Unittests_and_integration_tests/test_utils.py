#!/usr/bin/env python3
"""
Testing the utils.py module
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Testing access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'Can\'t find path in empty map'),
        ({"a": 1}, ("a", "b"), 'path b not present'),
        ])
    def test_access_nested_map_exception(self, nested_map, path, msg):
        with self.assertRaises(KeyError) as c:
            access_nested_map(nested_map, path)
        self.assertEqual(str(c.exception), msg)


if __name__ == '__main__':
    unittest.main()
