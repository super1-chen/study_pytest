#!/bin/python
#-*- encoding: utf8 -*-
# desc: bisect_example.copy()


def bisect_left(arr, k):
    """_summary_

    Args:
        arr (_type_): _description_
        key (_type_): _description_
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right + 1) // 2
        if arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return left

def bisect_right(arr, k):
    """_summary_

    Args:
        arr (_type_): _description_
        key (_type_): _description_
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right + 1) // 2
        if arr[mid] <= k:
            left = mid + 1
        else: # arr[mid] > k
            right = mid - 1
    return left


    
    
    