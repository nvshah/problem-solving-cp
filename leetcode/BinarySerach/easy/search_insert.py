# https://leetcode.com/problems/search-insert-position/

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    s, e = 0, len(nums)-1
    while s <= e:
        m = s + (e - s) // 2
        elem = nums[m]
        if elem == target:
            return m 
        elif target > elem:
            s += 1
        else:
            e -= 1
    return s