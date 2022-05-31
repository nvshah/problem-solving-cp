# https://www.lintcode.com/problem/508/
from typing import List
from itertools import pairwise

'''
Description

Given an unsorted array nums, reorder it in-place such that
'''


def wiggle_sort(nums: List[int]):
    for c, n in pairwise(range(len(nums))):
        cur, nxt = nums[c], nums[n]
        if c % 2 == 0:
            if cur > nxt: # swap
                nums[c], nums[n] = nums[n], nums[c]
        else:
            if nxt > cur: # swap
                nums[c], nums[n] = nums[n], nums[c]

nums = [1,5,1,1,6,4]    
nums = [1,3,2,2,3,1]
wiggle_sort(nums)
print(nums)
