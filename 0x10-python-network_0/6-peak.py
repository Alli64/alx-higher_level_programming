#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""



def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    hi = None
    for element in list_of_integers:
        if hi is None or hi < element:
            hi = element
    return hi
