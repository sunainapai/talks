# testapp.py

import unittest
from unittest import mock

import app


class AppTest(unittest.TestCase):

    @mock.patch('requests.get')
    def test_get_stars(self, mock_get):
        app.get_stars('', '')
        mock_get.assert_called()

    @mock.patch('requests.get')
    def test_get_stars2(self, mock_get):
        app.get_stars('', '')
        mock_get.assert_called_once()

    @mock.patch('requests.get')
    def test_get_stars3(self, mock_get):
        owner, repo = 'foo', 'bar'
        url = 'https://api.github.com/repos/' + owner + '/' + repo
        app.get_stars(owner, repo)
        mock_get.assert_called_once_with(url)
