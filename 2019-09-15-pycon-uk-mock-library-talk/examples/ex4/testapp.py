# testapp.py

import unittest
from unittest import mock

import app


class AppTest(unittest.TestCase):

    @mock.patch('requests.get')
    def test_get_stars(self, mock_get):
        owner, repo = 'foo', 'bar'
        url = f'https://api.github.com/repos/{owner}/{repo}'
        key = 'stargazers_count'
        app.get_stars(owner, repo)
        expected = [mock.call(url), mock.call().json(),
                    mock.call().json().get(key)]
        self.assertEqual(mock_get.mock_calls, expected)

    @mock.patch('requests.get')
    def test_get_stars_good(self, mock_get):
        owner, repo = 'foo', 'bar'
        url = f'https://api.github.com/repos/{owner}/{repo}'
        key = 'stargazers_count'
        app.get_stars(owner, repo)
        expected = mock.call(url).json().get(key).call_list()
        self.assertEqual(mock_get.mock_calls, expected)
