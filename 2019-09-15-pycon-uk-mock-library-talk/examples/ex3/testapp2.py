# testapp.py

import unittest
from unittest import mock

import app


class AppTest(unittest.TestCase):

    @mock.patch('requests.get', autospec=True)
    def test_get_stars(self, mock_get):
        app.get_stars('', '')
        mock_get.assert_called()
