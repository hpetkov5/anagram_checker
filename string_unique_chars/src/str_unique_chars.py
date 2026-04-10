'''
This module provides a function to check if all characters in a string are unique.
'''
def has_all_unique_chars(string1: str) -> bool:
    '''
    This function takes a string as input and checks if all characters in the string are unique.
    :param s: The input string.
    :return: True if all characters are unique, False otherwise.
    '''
    checked_chars = []
    for char in string1:
        if char in checked_chars:
            return False
        checked_chars.append(char)
    return True
