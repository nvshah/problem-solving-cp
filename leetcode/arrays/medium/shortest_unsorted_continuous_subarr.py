# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
from typing import List

def findUnsortedSubarray1(nums: List[int]) -> int:
    # Find smallest & biggest among all out of order nums
    minOutOfOrder = float('inf') 
    maxOutOfOrder = float('-inf')

    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]: # AMiss 
            # ! Out of order found in a Pair always !!
            maxOutOfOrder = max(maxOutOfOrder, nums[i])
            minOutOfOrder = min(minOutOfOrder, nums[i+1])
    
    if minOutOfOrder == float('inf'):
        return 0 # no out of order nums in nums
    
    # Find correct boundaries of subarr for Out-Of-Order nums 
    leftPos, rightPos = 0, len(nums)-1 

    while minOutOfOrder >= nums[leftPos]:  # In Left Part
        leftPos += 1
    
    while maxOutOfOrder <= nums[rightPos]: # In Right Part
        rightPos -= 1
    
    return rightPos - leftPos + 1 

def findUnsortedSubarray2(nums: List[int]) -> int:
    n = len(nums)
    # 1. Find the First Incorrect Loc from Left Side
    l = 0
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            l = i
            break
    else:
        return 0
    
    # 2. Find the First Incorrect Loc from Right Side
    r = 0
    for i in range(n-1, 0, -1):
        if nums[i] < nums[i-1]:
            r = i
            break
    else:
        return 0
            
    # 3. Find min & max in window [l, r]
    small, big = min(nums[l:r+1]), max(nums[l:r+1])
            
    # 4. find correct pos of sub-array begin
    begin = l
    for i in range(l):
        if small < nums[i]:
            begin = i
            break
            
    # 4. find correct pos of sub-array end
    end = r
    for i in range(n-1, r, -1):
        if big > nums[i]:
            end = i
            break
    
    return end-begin+1


# --- TEST 

nums = [1,3,5,4,2]
ans = findUnsortedSubarray1(nums) 