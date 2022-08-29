# https://leetcode.com/problems/minimum-interval-to-include-each-query/

from typing import List
import heapq

'''
Concept :
HeapQ + Sliding Window
'''

def minInterval(intervals: List[List[int]], queries: List[int]) -> List[int]:
    '''O(nlogn + qlogq)'''
    tQ = len(queries)  # total Queries
    tI = len(intervals) # total intervals

    # 0.1 sort the intervals as per the start point
    intervals.sort()

    # 0.2 get the queries positions after sorting (ie argsort)
    pos = sorted(range(tQ), key=queries.__getitem__)

    # result 
    res = [-1]*tQ # holds the intervals answer corresponding to [queries]
    r = 0 # current interval pointer (Sliding Window moving Right Side Pointer)
    
    # Kinda emulates Sliding Window (via eliminating the ineligible candidates)
    # -> holds the candidates for intervals
    minHeap = [] # (length, endPoint)

    for i in pos:
        q = queries[i] # query 

        # 1. Add all eligible candidates (intervals)
        while r != tI and intervals[r][0] <= q:
            s, e = intervals[r]
            heapq.heappush(minHeap, (e-s+1, e))
            r += 1 # move ahead
        
        # 2. Swipe Out all ineligible candidates (ie from Left Side)
        while minHeap and minHeap[0][1] < q:
            heapq.heappop(minHeap)

        # 3. Assign most suitable interval length
        if minHeap:
            res[i] = minHeap[0][0]
    
    return res 


