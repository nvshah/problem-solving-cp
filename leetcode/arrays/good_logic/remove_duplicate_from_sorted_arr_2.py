# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
from typing import List


def removeDuplicates(nums: List[int]) -> int:
    l, r = 0, 0
    total = len(nums)
    while r < total:
        # visit current deck of same members
        cnt = 1
        elm = nums[r]
        while r+1 < total and elm == nums[r+1]:
            cnt, r = cnt+1, r+1
        
        for _ in range(min(2, cnt)):
            nums[l] = elm  # Shift elem in current deck to avail pos ie {l}
            l += 1  # next avail pos
        
        r += 1  # check for next deck
    return l
                
                
            
                
                
        
                