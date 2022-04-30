# https://leetcode.com/problems/find-pivot-index/

from typing import List


def pivotIndex(nums: List[int]) -> int:
    r = sum(nums) # r -> right side sum
    l = 0  # l -> left side sum
    
    for i, n in enumerate(nums):
        # {i} as the pivot
        r -= n
        if l == r:
            return i
        l += n
        
    return -1