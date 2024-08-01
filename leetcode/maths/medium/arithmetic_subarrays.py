# https://leetcode.com/problems/arithmetic-subarrays/description/
from typing import List 
from itertools import pairwise

# O(nlogn) time | O(1) space
def check1(arr):
    '''Sort'''
    arr.sort()
    if len(arr) < 2: return True 

    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return False 
    
    return True

# O(n) time | O(n) space
def check2(arr):
    '''Math
        first = a
        last = a + (n-1)d

        d = (last - first) / (n-1)
    '''
    n = len(arr)
    if n < 2: return True 
    arrSet = set(arr)

    first, last = min(arr), max(arr)
    d = (last - first) / (n-1) # diff

    a = first 
    for i in range(1, n): # construct all elem in AP
        if a + (i*d) not in arrSet: return False 
    
    return True 

def checkArithmeticSubarrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    return [check2(nums[le:ri+1]) for le, ri in zip(l, r)]


# Test

nums, l, r = [4,6,5,9,3,7], [0,0,2], [2,3,5]
ans = checkArithmeticSubarrays(nums, l, r)
print(ans)