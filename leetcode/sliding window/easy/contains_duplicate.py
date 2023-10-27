# https://leetcode.com/problems/contains-duplicate/
from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    '''Sliding Window'''
    l = 0
    window = set()
    for r in range(len(nums)):
        if r - l > k: # valid window constraints (ie abs(i-j) <= k)
            # shrink the window
            window.remove(nums[l])
            l += 1
        if nums[r] in window:
            return True 
        window.add(nums[r])
    return False