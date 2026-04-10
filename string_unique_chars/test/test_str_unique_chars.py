'''
Unit tests for the string unique characters function.

This module uses the unittest framework to test the functionality of the has_all_unique_chars function.
'''
import unittest
from string_unique_chars.src.str_unique_chars import has_all_unique_chars


class TestHasAllUniqueChars(unittest.TestCase):

    def test_has_all_unique_chars(self):
        self.assertTrue(has_all_unique_chars("abcdefg"))

    def test_has_duplicate_chars(self):
        self.assertFalse(has_all_unique_chars("hello"))

    def test_empty_string(self):
        self.assertTrue(has_all_unique_chars(""))

    def test_single_character(self):
        self.assertTrue(has_all_unique_chars("a"))


if __name__ == "__main__":
    unittest.main()