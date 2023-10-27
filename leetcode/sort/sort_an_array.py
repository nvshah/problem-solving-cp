# https://leetcode.com/problems/sort-an-array/description/
from typing import List

# Merge Sort (O(n logn))
def sortArray(nums: List[int]) -> List[int]:

    def merge(arr, l, m, r):
        '''merge sorted halfs (ie [l,m] & [m+1,r]) to form single sorted seq'''
        left, right = arr[l:m+1], arr[m+1:r+1]
        sizeL, sizeR = len(left), len(right)
        i, j, k = l, 0, 0  # pointers to original, left, right

        while j < sizeL or k < sizeR:
            if j == sizeL:
                arr[i], k = right[k], k+1
            elif k == sizeR or left[j] <= right[k]:
                arr[i], j = left[j], j+1
            else:
                arr[i], k = right[k], k+1
            i += 1

    # O(nlogn) time | O(n) space
    def mergeSort(arr, l, r):
        '''recursively sort the [arr] inplace using divide & conquer approach'''
        if l == r: return arr 

        m = (l + r) // 2
        mergeSort(arr, l, m)  # left half
        mergeSort(arr, m+1, r) # right half

        merge(arr, l, m, r) # merge 2 halfs (ie [l,m], [m+1,r])

    mergeSort(nums, 0, len(nums)-1)
    return nums

nums = [5,2,3,1]
sortArray(nums)
