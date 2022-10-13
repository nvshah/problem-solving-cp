# https://leetcode.com/problems/largest-perimeter-triangle/

from heapq import heapify, heappop
from typing import List


def largestPerimeter(nums: List[int]) -> int:
    maxHeap = [-n for n in nums]
    heapify(maxHeap)
    
    a = -heappop(maxHeap)
    b = -heappop(maxHeap)
    while maxHeap:
        c = -heappop(maxHeap)
        if b + c > a: return (a + b + c)
        a, b = b, c
    
    return 0