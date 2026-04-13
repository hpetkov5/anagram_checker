'''
This module provides a function to get the current time in a specific format.
'''
import datetime as dt

def get_current_time() -> str:
    '''
    This function returns the current time in the format "HH:MM:SS.F".
    :return: A string representing the current time.
    '''
    return dt.datetime.now().strftime("%H:%M:%S.%f")
