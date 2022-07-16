# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List
from collections import defaultdict


def longestConsecutive(nums: List[int]) -> int:
    visited = defaultdict(bool)
    nums_set = set(nums)
    ans = 0  # length of longest consecutive seq
    for n in nums:
        if visited[n]:
            continue 
        l = n-1 # left neighbour
        if l not in nums_set: # n will be start elem of one of consecutive seq
            size = 1 # n itself
            r = n+1 # right neighbour
            while r in nums_set: # till sequence exists
                size += 1
                visited[r] = True
                r += 1
            ans = max(size, ans)
    
    return ans

def longestConsecutive2(nums: List[int]) -> int:
    nums_set = set(nums)
    ans = 0  # length of longest consecutive seq
    for n in nums:
        if n-1 not in nums_set: # n will be start elem of one of consecutive seq
            length = 0 # n itself
            while n + length in nums_set: # till sequence exists
                length += 1
            ans = max(length, ans)
    
    return ans

a = longestConsecutive([100,4,200,1,3,2])
print(a)