import heapq
from typing import List
'''
Que
You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
'''

def swimInWater(grid: List[List[int]]) -> int:
    N = len(grid)
    if N==1: return grid[0][0]

    # first pos -> max-Height in that path or time to cross this pos ie (row, col)
    minHeap = [(grid[0][0], 0, 0)] # (max-height|time, row, col)
    visit = {(0,0)}
    directions = [(0,1), (1, 0), (0,-1), (-1,0)]
    

    while minHeap:
        t, r, c = heapq.heappop(minHeap)

        for dr, dc in directions:
            i, j = r+dr, c+dc   # neighbor (i, j)
            if (i<0 or j<0 or i==N or j==N or
                (i, j) in visit
                ):
                continue
            maxTime = max(t, grid[i][j])
            if i == N-1 and j == N-1:
                return maxTime
            heapq.heappush(minHeap, (maxTime, i, j))
            visit.add((i,j))


