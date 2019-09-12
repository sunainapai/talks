# testapp.py

import unittest
from unittest import mock

import app


class AppTest(unittest.TestCase):

    @mock.patch('app.getsize')
    def test_total_size(self, mock_getsize):
        mock_getsize.return_value = 10
        total = app.get_total_size(['', ''])
        self.assertEqual(total, 20)
