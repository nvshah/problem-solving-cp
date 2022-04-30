# https://leetcode.com/problems/subarray-sum-equals-k/

'''
Given an array of integers nums and an integer k, 
return the total number of continuous subarrays whose sum equals to k.

'''

from typing import List
from collections import defaultdict


def subarraySum(nums: List[int], k: int) -> int:
    '''
    Logic ;- O(n)
    Idea :- Prefix Elimination method
            For given substring check first if we could achieve sum somehow 
            by deducting or adjustment (ie remvoing prefix & keeping suffix s.t. suffix sum = k)
    '''
    total_cnt = currSum = 0
    # mapp the number of ways prefix can be achieved for given substring
    # sum of 0 can be available initially (assumption)
    #prefix_cnt = {0:1}  
    prefix_cnt = defaultdict(int)
    prefix_cnt[0] = 1 # for sum = 0 assume achieved without any number => 1 way
    for n in nums:
        currSum += n 
        prefix = currSum - k
        # adjustment s.t.prefix can be removed with suffix = t remains
        total_cnt += prefix_cnt[prefix] # prefix can be removed in diff ways denoted by the map
        prefix_cnt[currSum] += 1 # 1 more way to achieve prefix = currSum is recorded

    return total_cnt


# def findMinimalSubArr(nums: List[int], k: int) -> int:
#     '''
#         Task : Find the minimal sub array s.t sum = k
#     '''
#     res = []
#     curr_sum = 0
#     prefix_length = defaultdict(int)

#     for i, n in enumerate(nums):
#         curr_sum += n 
#         pre = curr_sum - k 
#         prefix_length

a = subarraySum([5,5], 10)
print(a)