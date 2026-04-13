'''
This module provides a function to subtract five days from the current date.
'''
import datetime as dt

def subtract_five_days() -> str:
    '''
    This function subtracts five days from the current date and returns the result in the format "YYYY-MM-DD".
    :return: A string representing the date five days ago.
    '''
    five_days_ago = dt.datetime.now() - dt.timedelta(days=5)
    return five_days_ago.strftime("%Y-%m-%d")
