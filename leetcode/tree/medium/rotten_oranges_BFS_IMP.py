# https://leetcode.com/problems/rotting-oranges/

from typing import List



'''
 Impl : using BFS as we need simultaneous count of all rotten oranges in single min
'''
from collections import deque

def orangesRotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    time = fresh = 0
    dq = deque() # add the coordinates of rotten oranges

    # count total number of fresh oranges & add rotten oranges to queue of bfs
    for i in range(rows):
        for j in range(cols):
            v = grid[i][j]
            if v == 1:
                fresh += 1
            elif v == 2: # rotten (initially)
                dq.append((i, j)) 

    directions = [(0,1), (0,-1), (1,0), (-1,0)] # right, left, top, bottom

    print(dq)

    # loop till all rotten oranges visited or all fresh oranges are converted into rotten one
    while dq and fresh > 0:
        # check for each rotten orange in current time tick
        size = len(dq)
        for i in range(size):
            r, c = dq.popleft() # coordinates of rotten orange in grid
            # check for any neighbor fresh orange in all directions
            for x,y in directions:
                m1, m2 = r+x, c+y
                if (0 <= m1 < rows) and (0 <= m2 < cols):
                    if grid[m1][m2] == 1: # fresh orange
                        grid[m1][m2], fresh = 2, fresh-1 # fresh orange -> corrupt orange
                        dq.append((m1, m2))
        time += 1
    
    if fresh:
        return -1
    else:
        return time

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))