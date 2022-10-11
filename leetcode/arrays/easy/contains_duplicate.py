# https://leetcode.com/problems/contains-duplicate-ii/

from collections import defaultdict
from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    idx_map = {}  # map for right most index of number
        
    for i, num in enumerate(nums):
        if num in idx_map:
            j = idx_map[num]  # latest idx for {num} till now
            if abs(i-j) <= k: return True
        
        idx_map[num] = i  # update latest idx for {num}
    
    return False
                
                
            