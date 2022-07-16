# https://leetcode.com/problems/wiggle-subsequence/

from itertools import pairwise
from math import copysign
from typing import List


def wiggleMaxLength(nums: List[int]) -> int:
    n = len(nums)
    diff = [nums[i] - nums[i-1] for i in range(1, n) if nums[i]!=nums[i-1]]
    
    # Eg [1, 1, 1] -> [0, 0]
    if not diff: return 1
    
    cnt = 2 # first 2 nums (atleast present as valid subseq)
    for d1, d2 in pairwise(diff):
        # In case of consecutive same sign we will consider last sign
        # Eg 1, 4, 8, 6, 3 -> 1,8,3
        if copysign(1, d1) != copysign(1, d2):
            cnt += 1
    
    return cnt

def wiggleMaxSequence(nums: List[int]) -> int:
    n = len(nums)
    #diff = [nums[i] - nums[i-1] for i in range(1, n) if nums[i]!=nums[i-1]]
    stack = []

    if n <= 1: return n

    stack = [nums[0]]  # selected elements
    lsign = 0   # last difference sign
    for n in nums[1:]:
        cdiff = n - stack[-1]  # current difference
        if cdiff == 0:
            continue 
        
        sign = copysign(1, cdiff)  # current sign

        if sign == lsign:
            if sign == 1:  # increasing 
                stack[-1] = max(stack[-1], n) 
            else:  # decreasing
                stack[-1] = min(stack[-1], n)
        else:  
            # alternating
            stack.append(n)
        
        lsign = sign
    
    return stack

# + + - - 
nums = [1,17,5,10,13,15,10,5,16,8]
nums = [1,2,3,4,5,6,7,8,9]
s = wiggleMaxSequence(nums) 
print(s)