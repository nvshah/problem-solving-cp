# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/description/

from typing import List
import heapq

'''
Greedy Approach : Try filling the bags that required minimum rocks to be full.
'''

def maximumBags(capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
    # Heap is nothing but Priority Queue
    que = [cap-fill for cap, fill in zip(capacity, rocks)]
    heapq.heapify(que)
    cnt = 0
    while que and additionalRocks:
        rem = heapq.heappop(que)

        if rem:
            if rem > additionalRocks: 
                return cnt
            additionalRocks -= rem 
        
        cnt += 1
    return cnt

capacity = [2,3,4,5]
rocks = [1,2,4,4]
additionalRocks = 2

ans = maximumBags(capacity, rocks, additionalRocks)
print(ans)



