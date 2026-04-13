'''
Unit tests for the Fibonacci function.

This module uses the pytest framework to test the functionality of the Fibonacci class.
'''

from fibonacci.src.fibonacci import Fibonacci

def test_fibonacci():
    fib = Fibonacci()
    expected_output = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert fib.fibonacci() == expected_output

def test_print_fibonacci(capsys):
    fib = Fibonacci()
    fib.print_fibonacci()
    captured = capsys.readouterr()
    expected_output = "The first 10 Fibonacci numbers are: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n"
    assert captured.out == expected_output
