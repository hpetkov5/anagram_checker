'''
This module provides a function to find the missing number in an array from 10 to 20.
'''

def find_missing_number(array: list) -> int:
    '''
    This function takes an array of integers and returns the missing number from the range 10 to 20.
    :param array: A list of integers.
    :return: The missing integer from the range 10 to 20.
    '''
    full_array = [i for i in range(10, 21)]
    for num in full_array:
        if num not in array:
            return num
    return None
