# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import List
import heapq
from math import sqrt
import itertools as it

def euc_dist(p):
    return sqrt(p[0]**2 + p[1]**2)

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    return heapq.nsmallest(k, points, key = euc_dist)

def kClosest2(points: List[List[int]], k: int) -> List[List[int]]:
    def euc_dist(x1, x2):
        return sqrt(x1**2 + x2**2)
    minHeap = [(euc_dist(*p), i) for i, p in enumerate(points)]
    heapq.heapify(minHeap)
    res = []
    for _ in range(k):
        d, i = heapq.heappop(minHeap)
        res.append(points[i])
    return res



points = [[1,3],[-2,2]]
k = 1

points = [[3,3],[5,-1],[-2,4]]
k = 2

ans = kClosest(points, k)
print(ans)