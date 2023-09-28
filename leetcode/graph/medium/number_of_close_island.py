# https://leetcode.com/problems/number-of-closed-islands/

from typing import List
from itertools import product


def closedIsland(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])

    def markVisit(r, c):
        grid[r][c] = 2  # 2 -> visited
    
    def isVisited(r, c):
        return grid[r][c] == 2

    def isClose(r, c):
        '''
        # use dfs technique to identify if land (r,c) is part of close island or not !
        returns: 1 if its closed else 0
        '''
        # STOP - Cases

        # check if land is lying on fence (ie permiter)
        if r < 0 or c < 0 or r == ROWS or c == COLS: 
            return 0  # as its open to outside land so cannto be close anywhere

        # check if its water
        if grid[r][c] == 1:
            return 1  # if its water then its already closed (given)
        

        # Avoid Infinite Loop - Case
        # check if land visited earlier
        if isVisited(r, c):
            # (r, c) is visited & part of current chunk exploration
            # NOTE: land would be visited once during exploration

            # Until its not discovered that land is connected to outside, we'll consider it as close
            # (inorder to make other adjacent visits successful) 
            return 1

        # mark visit
        markVisit(r, c)

        # explore adjacent pieces
        left = isClose(r, c-1)
        right = isClose(r, c+1)
        top = isClose(r-1, c)
        down = isClose(r+1, c)

        # If outside of island is explorable by any of adjacent then this current exploration is not closed
        # Hence this chunk, if needs to be close (ie isolated) then all adjacen should abnegate from openness to outside !
        return left & right & top & down 
        #return min(l, r, t, d)
    
    res = 0
    for i, j in product(range(ROWS), range(COLS)):
        # Check if its unvisited land
        if grid[i][j] == 0:
            print(f'visiting :- {(i, j)}')
            t = isClose(i, j)
            print('Status' f'{t}')
    return res 

grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
closedIsland(grid)
