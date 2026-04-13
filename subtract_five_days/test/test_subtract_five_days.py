'''
Unit tests for the current time function.

This module uses the unittest framework to test the functionality of the get_current_time function.
'''

from freezegun import freeze_time
from subtract_five_days.src.subtract_five_days import subtract_five_days

@freeze_time("2026-01-10")
def test_subtract_five_days():
    expected_date = "2026-01-05"
    assert subtract_five_days() == expected_date
