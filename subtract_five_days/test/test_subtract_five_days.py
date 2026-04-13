'''
Unit tests for the current time function.

This module uses the unittest framework to test the functionality of the get_current_time function.
'''

import unittest
from freezegun import freeze_time
from subtract_five_days.src.subtract_five_days import subtract_five_days


class TestSubtractFiveDays(unittest.TestCase):

    @freeze_time("2026-01-10")
    def test_subtract_five_days(self):
        expected_date = "2026-01-05"
        self.assertEqual(subtract_five_days(), expected_date)
