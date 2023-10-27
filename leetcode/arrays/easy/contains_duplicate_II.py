# https://leetcode.com/problems/contains-duplicate-ii/

from collections import defaultdict
from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    '''MAP'''
    idx_map = {}  # map for right most index of number
        
    for i, num in enumerate(nums):
        if num in idx_map:
            j = idx_map[num]  # latest idx for {num} till now
            if abs(i-j) <= k: return True
        
        idx_map[num] = i  # update latest idx for {num}
    
    return False

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
                
            