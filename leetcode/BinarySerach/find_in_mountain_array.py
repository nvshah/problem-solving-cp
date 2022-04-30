
# https://leetcode.com/problems/find-in-mountain-array/

from typing import List


def peakIndexInMountainArray(arr: List[int]) -> int:
    '''
        Find the peak element in Mountain Array

    '''
    s, e = 0, len(arr)-1
    while s != e:  # or s < e
        m = s + (e-s)//2
        if arr[m] > arr[m+1]:
            # search in left part (i.e m can be a candidate for peak val)
            e = m
        else:
            # search in right part (i.e m+1 can be a candidate for peak val)
            s = m+1
    return s


def orderAgnosticBinarySearch(arr, target, start, end, nonDecreasing):
    '''
    Binary Search - Basic Implementation i.e Order Agnostic Binary Search
    Assuming arr is sorted
    '''
    if not arr:
        raise Exception("array is empty")
    #start, end = 0, len(arr) - 1

    if arr[0] == arr[-1]:
        # All elements in {arr} are same
        return 0 if arr[0] == target else -1

    # if not nonDecreasing:
    #     nonDecreasing = arr[0] < arr[-1]

    if nonDecreasing:
        # {arr} is in non-decreasing Order
        while start <= end:
            mid = start + ((end - start) // 2)
            if target > arr[mid]:
                # Search in Right Part
                start = mid + 1
            elif target < arr[mid]:
                # Search in Left Part
                end = mid - 1
            else:
                return mid
    else:
        # {arr} is in non-increasing Order
        while start <= end:
            mid = start + ((end - start) // 2)
            if target > arr[mid]:
                # Search in Left Part
                end = mid - 1
            elif target < arr[mid]:
                # Search in Right Part
                start = mid + 1
            else:
                return mid
    return -1


def findInMountainArray(target: int, mountain_arr: 'MountainArray') -> int:
    peakIdx = peakIndexInMountainArray(mountain_arr)

    if peakIdx == target:
        return peakIdx

    # Search in Left part i.e non-decreasing part
    idx = orderAgnosticBinarySearch(
        mountain_arr,
        target,
        0,
        peakIdx-1,
        nonDecreasing=True)
    if idx == -1:
        # search in Right part i.e increasing part
        idx = orderAgnosticBinarySearch(
            mountain_arr,
            target,
            peakIdx+1,
            len(mountain_arr)-1,
            nonDecreasing=False,
        )

    return idx
