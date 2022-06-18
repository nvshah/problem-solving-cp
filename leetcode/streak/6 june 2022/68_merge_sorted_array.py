# https://leetcode.com/problems/merge-sorted-array/

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    m, n, k = m - 1, n - 1, m + n - 1

    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[k] = nums1[m]
            m -= 1
        else:
            nums1[k] = nums2[n]
            n -= 1
        k -= 1

    while n >= 0:
        nums1[k], k, n = nums2[n], n - 1, k - 1