'''
Unit tests for the anagram checker function.

This module uses the unittest framework to test the functionality of the are_anagrams function.
'''

import unittest
from anagram_checker.src.anagram_checker import are_anagrams


class TestAnagramChecker(unittest.TestCase):

    def test_anagrams(self):
        self.assertTrue(are_anagrams("listen", "silent"))

    def test_not_anagrams(self):
        self.assertFalse(are_anagrams("hello", "world"))

    def test_anagrams_with_spaces(self):
        self.assertTrue(are_anagrams("conversation", "voices rant on"))


if __name__ == '__main__':
    unittest.main()
