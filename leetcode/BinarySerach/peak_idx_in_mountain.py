# https://leetcode.com/problems/peak-index-in-a-mountain-array/


from typing import List


'''
Approach 1
Binary Search where peak value will be identified by middle element always during the process (as the length of arr is atleast 3)
'''


def peakIndexInMountainArray(arr: List[int]) -> int:
    '''
    arr -> Increasing then Decreasing after some peak val
        Idea -> binary search with custom condition i.e where 
        step-1) find middle idx
        step-2) if mid < mid + 1, search in right
        step-3) else search in left
        at the end start & end will point to max element in array
    '''
    s, e = 0, len(arr)-1
    while s != e:
        m = s + (e-s)//2
        if arr[m] > arr[m+1]:
            # search in left part (i.e m can be a candidate for peak val)
            e = m
        else:
            # search in right part (i.e m+1 can be a candidate for peak val)
            s = m+1
    return s


'''
Approach 2
Binary Search where start & end will point to peak value at the end of process.
'''


def peakIndexInMountainArray_2(arr: List[int]) -> int:
    s, e = 0, len(arr)-1
    while s <= e:
        m = s + (e-s)//2
        if arr[m-1] < arr[m]:
            if arr[m] > arr[m+1]:
                return m  # Peak idx i.e arr[m-1] < arr[m] > arr[m+1]
            else:
                s = m+1  # search in right part
        else:
            e = m  # search in left part
    return s


arr = [0, 1, 0]  # 1

arr = [0, 2, 1, 0]  # 1

arr = [0, 10, 5, 2]  # 1

arr = [3, 4, 5, 1]  # 2

arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]  # 2

ans = peakIndexInMountainArray(arr)

print(ans)
