# https://leetcode.com/problems/sort-array-by-parity/
from typing import List

def sortArrayByParity(nums: List[int]) -> List[int]:
    # l, r = 0, len(nums)-1
    # while r > l:
    #     if nums[r] % 2 == 0: # even number on LHS
    #         nums[r], nums[l] = nums[l], nums[r]
    #         l += 1
    #     else:  # odd number on RHS
    #         r -= 1
    # return nums
    
    nums.sort(key= lambda x: x & 1)
    return nums