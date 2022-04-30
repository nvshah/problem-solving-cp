# https://leetcode.com/problems/search-insert-position/

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    s, e = 0, len(nums)-1
    while s <= e:
        m = s + (e-s)//2
        if target > m:
            s = m + 1
        elif target < m:
            e = m - 1
        else:
            return m
    return s
