# https://leetcode.com/problems/number-of-enclaves/

from typing import List
from itertools import chain, repeat, starmap


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # compute total lands
        total_lands = sum(chain.from_iterable(grid))

        # explore only border lands & its reachable lands
        borders = chain(
            zip(repeat(0), range(cols)), # First Row
            zip(repeat(rows-1), range(cols)), # Last Row
            zip(range(rows), repeat(0)),  # First Column
            zip(range(rows), repeat(cols-1)), # Last Column
        )

        visited = set() # (i,j) => visited cell
        def dfs(i, j):
            '''return the total land connected to cell (i,j) (including (i,j)), if its a land '''
            if i<0 or i==rows or j<0 or j==cols:
                return 0 # not a grid
            if not grid[i][j]:
                return 0 # not a land
            if (i,j) in visited:
                return 0
            
            cnt = 1 # As this cell (i,j) is a land
            visited.add((i,j))
            # Find connected land count from neighbors
            for ni, nj in [(0,1), (1,0), (0,-1), (-1,0)]: # [Up, left, Down, Right]
                cnt += dfs(i+ni, j+nj)
            return cnt

        border_reachable_lands = sum(starmap(dfs, borders))

        return total_lands - border_reachable_lands
    

