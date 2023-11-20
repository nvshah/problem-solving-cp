# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
from typing import List 
# import heapq
from functools import reduce

def maximumElementAfterDecrementingAndRearranging(arr: List[int]) -> int:
    arr.sort() 
    return reduce(lambda prev, cur: min(prev+1, cur), arr, 0)

def maximumElementAfterDecrementingAndRearranging(arr: List[int]) -> int:
    arr.sort() 
    prev = 0
    for e in arr:
        prev = min(prev+1, e)
    return prev 

# def maximumElementAfterDecrementingAndRearranging(arr: List[int]) -> int:
#     MAX = max(arr)
#     heapq.heapify(arr)

#     prev = 0

#     while arr:
#         ele = heapq.heappop(arr)

#         cand = prev + 1

#         if cand == MAX: return MAX 
#         prev = min(cand, ele)
    
#     return prev 