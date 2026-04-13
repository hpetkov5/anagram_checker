'''
Unit tests for the factorial functions.

This module uses the pytest framework to test the functionality of the factorial functions.
'''
import pytest
from factorial.src.factorial import factorial_iterative, factorial_recursive

@pytest.mark.parametrize("fact_input, expected", [
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
])
def test_factorial_iterative(fact_input, expected):
    assert factorial_iterative(fact_input) == expected

@pytest.mark.parametrize("fact_input, expected", [
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
])
def test_factorial_recursive(fact_input, expected):
    assert factorial_recursive(fact_input) == expected
