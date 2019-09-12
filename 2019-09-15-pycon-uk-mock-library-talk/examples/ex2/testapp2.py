# testapp.py

import unittest
from unittest import mock

import app


class AppTest(unittest.TestCase):

    @mock.patch('requests.get')
    def test_get_stars(self, mock_get):
        owner, repo = 'foo', 'bar'
        url = f'https://api.github.com/repos/{owner}/{repo}'
        mock_get.return_value.json.return_value = {'stargazers_count': 5}
        app.get_stars(owner, repo)
        mock_get.assert_called_once_with(url)

    @mock.patch('requests.get')
    def test_get_stars_good(self, mock_get):
        owner, repo = 'foo', 'bar'
        url = f'https://api.github.com/repos/{owner}/{repo}'
        # --mock_get.return_value.json.return_value = {'stargazers_count': 5}--
        app.get_stars(owner, repo)
        mock_get.assert_called_once_with(url)
