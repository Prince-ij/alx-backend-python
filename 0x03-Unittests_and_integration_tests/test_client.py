#!/usr/bin/env python3
""" test GithubOrgClient """
import unittest
from unittest.mock import patch
from utils import memoize, get_json, access_nested_map
from parameterized import parameterized
from client import GitHubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ testing org """

    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'})
        ])
    @patch('client.get_json', return_value={'login': 'test'})
    def test_org(self, org_name, expected, mock_get_json):
        """ test_org implementing """
        client = GitHubOrgClient(org_name)
        self.assertEqual(client.org, expected)
        labu = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(labu)


if __name__ == '__main__':
    unittest.main()
