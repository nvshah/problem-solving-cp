# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

from heapq import nlargest
from statistics import median
from typing import List


def minMoves2(nums: List[int]) -> int:
    n = len(nums)
    m = (n+1)//2
    
    l = nlargest(m, nums)
    
    e = l[-1]  # middle element

    # p = min(range(len(nums)), key=lambda i: abs(nums[i]-m))
    # e = nums[p]
    return sum(abs(n-e) for n in nums)

def minMoves2_2(nums: List[int]) -> int:

    e = int(median(nums))
    
    return sum(abs(n-e) for n in nums)