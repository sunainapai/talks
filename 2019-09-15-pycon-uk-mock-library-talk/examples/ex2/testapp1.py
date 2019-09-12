# testapp.py

import unittest
from unittest import mock

import app


class AppTest(unittest.TestCase):

    @mock.patch('requests.get')
    def test_get_stars(self, mock_get):
        mock_response = mock.Mock()
        mock_response.json.return_value = {'stargazers_count': 5}
        mock_get.return_value = mock_response
        stars = app.get_stars('', '')
        self.assertEqual(stars, 5)

    @mock.patch('requests.get')
    def test_get_stars_good(self, mock_get):
        mock_get.return_value.json.return_value = {'stargazers_count': 5}
        stars = app.get_stars('', '')
        self.assertEqual(stars, 5)
