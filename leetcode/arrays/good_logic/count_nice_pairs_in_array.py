# https://leetcode.com/problems/count-nice-pairs-in-an-array/

from typing import List
from collections import defaultdict
from math import comb

def rev(n):
    res = 0 
    while n > 0:
        q, r = divmod(n, 10)
        res = res*10 + r 
        n = q 
    return res 

def countNicePairs(nums: List[int]) -> int:
    '''
        nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
         ||
        nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])

        IDEA: Running Combination | Prefix 
    '''
    freqs = defaultdict(int) 
    ans = 0

    for el in nums:
        k = el - rev(el)
        # pairs possible for {el} = # prev candidates having same key {k}
        ans += freqs[k]   # running comb() via prefix-map
        ans %= (10**9 + 7)
        freqs[k] += 1
    
    return ans % (10**9 + 7)

def countNicePairs2(nums: List[int]) -> int:
    '''
        nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
         ||
        nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])

        IDEA: Running Combination | Prefix 
    '''
    freqs = defaultdict(int) 

    for el in nums:
        k = el - rev(el)
        freqs[k] += 1
    
    #ans = sum([x*(x-1)//2 for x in freqs.values()]) # comb(n, 2)
    ans = sum([comb(x, 2) for x in freqs.values()]) # pairs for individual-key
    return ans % (10**9 + 7)

