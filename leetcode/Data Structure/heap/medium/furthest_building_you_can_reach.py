# https://leetcode.com/problems/furthest-building-you-can-reach/

from heapq import heappop, heappush
from typing import List


def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    n = len(heights)
    
    jumps = []  # min heap that let you find minimum jump
    
    for i in range(n-1):
        diff = heights[i+1] - heights[i]
        if diff <= 0: # no need of jump or climb
            continue
            
        # register possible jumpt
        heappush(jumps, diff)
        
        if(len(jumps) > ladders):
            # make smallest jump with bricks & rest climb with ladders
            j = heappop(jumps)
            bricks -= j  # use bricks to make that smallest jump
        
            if(bricks < 0): # exhausted & so cannot move further
                return i
    
    return n-1  # last building
        
        