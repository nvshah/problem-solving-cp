# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

import heapq
from typing import List

def kthLargestNumber(nums: List[str], k: int) -> str:
    nums = [-int(n) for n in nums] # So that max become smallest

    # now our goal is to remove k-1 smallest nums

    heapq.heapify(nums) # O(n) -> smallest at root ie at pos 0

    # Remove {k-1} small numbers from nums
    for i in range(k-1):
        heapq.heappop(nums)
    
    return -nums[0] # at root will be kth small num = - (kth large num)



def kthLargestNumber(nums: List[str], k: int) -> str:
    return heapq.nlargest(k, nums, key=int)[-1]