#!/usr/bin/python3
"""finds a peak in a list of integers"""



def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    list_i = list_of_integers
    if list_of_integers == []:
        return None
    size = len(list_i)

    first, last = 0, size - 1
    while first < last:
        mid = first + (last - first) // 2
        if list_i[mid] > list_i[mid - 1] and list_i[mid] > list_i[mid + 1]:
            return list_i[mid]
        if list_i[mid - 1] > list_i[mid + 1]:
            end = mid
        else:
            first = mid + 1
            return list_i[first]
