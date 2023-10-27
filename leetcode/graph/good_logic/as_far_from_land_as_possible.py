# https://leetcode.com/problems/as-far-from-land-as-possible/
from typing import List
from collections import deque
from itertools import compress, repeat, chain

'''
Idea :
Multi-Source BFS
Start from all lands (ie src) simultaneously reaching nearest water blocks

> Multi-Source BFS:
Instead of starting from 1 point, start from multiple points (ie Initialize Queue with multiple points) & then go for breadth
This way diff walker from lands will reach the nearby water blocks in earlier time &
The last block remaining in queue will be the furthest water block from all lands

'''

def maxDistance(grid: List[List[int]]) -> int:
    N = len(grid) # square
    idxs = [*range(N)]

    # Find all lands
    lands = chain.from_iterable(zip(repeat(i), compress(idxs, grid[i])) for i in idxs)
    # lands = []
    # for r in idxs:
    #     for c in idxs:
    #         if grid[r][c]:
    #             lands.append((r,c))

    # Queue for MultiSource BFS, where sources are lands
    queue = deque(lands) # #sources = #lands

    # NOTE: we will consider land at distance 1
    far = -1  # furthest distance covered so far from land -> water
    directions = ((0,1), (1,0), (0,-1), (-1, 0))

    # start discovery of water from multiple sources(ie lands)
    # * The last remain in [queue] will be the farthest water block from any lands
    while queue:
        r, c = queue.popleft()

        far = grid[r][c] # update distance

        for x, y in directions:
            i, j = r+x, c+y
            # check boundary 
            if min(i, j) < 0 or max(i, j) == N: continue 
            # check if its water
            if grid[i][j] == 0:
                queue.append((i,j)) 
                grid[i][j] = grid[r][c] + 1 # update distance to reach (i,j) from (r,c)
    
    if far > 1: # Discovered atleast water
        return far-1 # inorder to consider land as starting, do -1
    return -1 # didn't found Water








    

    print(queue)

grid = [[1,0,1],[0,0,0],[1,0,1]]
maxDistance(grid)