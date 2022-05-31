from typing import List
from itertools import pairwise

def wiggleSort(nums: List[int]) -> None:
    """
    INCOmPLETE
    """
    sz = len(nums)
    for c, n in pairwise(range(sz)):
        i = n
        while i < sz and nums[i] == nums[c]:
            i += 1
        
        # we can assume that inp arr has always valid ans
        nums[c], nums[i] = nums[i], nums[c]
        
        cur, nxt = nums[c], nums[n]
            
        if c % 2 == 0:  # even pos
            if cur > nxt: # swap
                nums[c], nums[n] = nums[n], nums[c]
        else:  # odd pos
            if nxt > cur: # swap
                nums[c], nums[n] = nums[n], nums[c]

nums = [1,4,3,4,1,2,1,3,1,3,2,3,3]
