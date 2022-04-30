# https://leetcode.com/problems/island-perimeter/
from typing import List

def islandPerimeter(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    visited = set()  # keep track of visited stripes of an island
    ''' Via DFS '''
    def dfs(i, j):
        # 1. out of boundaries
        if i < 0 or i == rows or j < 0 or j == cols:
            return 1

        # 2. visited or not
        if (i,j) in visited:  
            return 0            # accounted earlier
        
        # 3. Water (ie internal boundary)
        if grid[i][j] == 0:
            return 1

        # ! Thus current stripe is part of island
        
        # 4. Mark current stripe as visited
        visited.add((i,j))

        # 5. Search for connected stripes of island
        perim = dfs(i-1, j) # top
        perim += dfs(i, j+1) # right
        perim += dfs(i+1, j) # bottom
        perim += dfs(i, j-1) # left

        return perim

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # We found 1 piece of island, thus explore entire island (via DFS)
                return dfs(i, j)

    return 0 # no island present
                
