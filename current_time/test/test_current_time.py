'''
Unit tests for the current time function.

This module uses the unittest framework to test the functionality of the get_current_time function.
'''

import unittest
from freezegun import freeze_time
from current_time.src.current_time import get_current_time


class TestGetCurrentTime(unittest.TestCase):

    @freeze_time("2026-01-01 12:00:00")
    def test_get_current_time(self):
        expected_time = "12:00:00.000000"
        self.assertEqual(get_current_time(), expected_time)
