'''
This module provides a function to check if two strings are anagrams of each other.
'''

def are_anagrams(str1: str, str2: str) -> bool:
    '''
    This function takes two strings as input and checks if they are anagrams of each other.
    :param str1: The first string.
    :param str2: The second string.
    :return: True if the strings are anagrams, False otherwise.
    '''
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
