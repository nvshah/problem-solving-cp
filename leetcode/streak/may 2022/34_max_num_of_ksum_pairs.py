# https://leetcode.com/problems/max-number-of-k-sum-pairs/

from typing import List
from collections import Counter 

'''Approach 1'''
def a1(nums, k):
    freqs = Counter(nums)
    ans = 0
    while freqs:
        n1, f1 = freqs.popitem()  # pick any random number {n1}
        n2 = k-n1                 # find corresp correct pair {n2}
        if n2 == n1:          
            ans += f1 // 2        # if pair possess same num   
        else:
            f2 = freqs.pop(n2, 0) 
            ans += min(f1, f2)    # register cnt of pair possible

    return ans

'''Approach 2'''
def a2(nums, k):
    nums = sorted(nums)
    
    l, r = 0, len(nums)-1
    ans = 0
    while l < r:
        t = nums[l] + nums[r]
        if t > k:
            r -= 1
        elif t < k:
            l += 1
        else:
            ans += 1
            l += 1
            r -= 1
    return ans

def maxOperations(nums: List[int], k: int) -> int:
    #return a2(nums, k)
    return a1(nums, k)
            