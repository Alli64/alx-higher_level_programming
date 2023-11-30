#!/usr/bin/python3
"""finds a peak in a list of integers"""



def find_peak(list_of_integers):
    """function that finds a peak in a list of unsorted integers"""
    list_i = list_of_integers
    size = len(list_i)
    if list_i == [] or size == 0:
        return None

    if size == 1:
        return list_i[0]

    mid = int(size / 2)

    if mid != size - 1:
        if list_i[mid] > list_i[mid - 1] and list_i[mid] > list_i[mid + 1]:
            return list_i[mid]
    else:
        if list_i[mid] > list_i[mid - 1]:
            return list_i[mid]
        else:
            return list_i[mid - 1]

    if list_i[mid - 1] > list_i[mid]:
        list_ = list_i[0:mid]
    else:
        list_ = list_i[mid + 1:]

        return find_peak(list_)
