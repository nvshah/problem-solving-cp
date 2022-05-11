# https://leetcode.com/problems/132-pattern/
from typing import List

'''
Que
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.
'''

def find132pattern(nums: List[int]) -> bool:
    # Monotonic Decreasing Stack
    stack = []  # (num_j, minLeft)  // used to track `j` 
    # -> ie top elem of {decrStk} will be candidate for num_j
    
    curMin = nums[0] # min-left side val for current idx during traversal
    
    for k in nums[1:]:
        # find out proper {j}  // that stays on top of decreasing stack
        while stack and k >= stack[-1][0]: 
            stack.pop()
        
        # thus now nums[k] < nums[j], assured if j exists on stack !

        # check constraints
        if stack and k > stack[-1][1]:
            return True
        
        # add to stack
        stack.append((k, curMin))
        
        # -> now onwards k become candidate for j
        curMin = min(curMin, k) 
    
    return False