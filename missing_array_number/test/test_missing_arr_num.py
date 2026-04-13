'''
Unit tests for the current time function.

This module uses the pytest framework to test the functionality of find_missing_number function.
'''

import pytest
from missing_array_number.src.missing_array_number import find_missing_number

@pytest.mark.parametrize("array, expected_missing_number", [
    ([11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 10),
    ([10, 12, 13, 14, 15, 16, 17, 18, 19, 20], 11),
    ([10, 11, 13, 14, 15, 16, 17, 18, 19, 20], 12),
    ([10, 11, 12, 14, 15, 16, 17, 18, 19, 20], 13),
    ([10, 11, 12, 13, 15, 16, 17, 18, 19, 20], 14),
    ([10, 11, 12, 13, 14, 16, 17, 18, 19, 20], 15),
    ([10, 11, 12, 13, 14, 15, 17, 18, 19, 20], 16),
    ([10, 11, 12, 13, 14, 15, 16, 18, 19, 20], 17),
    ([10, 11, 12, 13, 14, 15, 16, 17, 19, 20], 18),
    ([10, 11, 12, 13, 14, 15, 16, 17, 18, 20], 19),
    ([10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 20)]
)
def test_find_missing_number(array, expected_missing_number):
    assert find_missing_number(array) == expected_missing_number

def test_find_missing_number_no_missing():
    array = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert find_missing_number(array) is None
