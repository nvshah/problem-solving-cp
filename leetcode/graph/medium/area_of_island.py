
# https://leetcode.com/problems/max-area-of-island/

from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    visit = set()
    
    def dfs(r, c):
        if r<0 or r>=m or c<0 or c>=n: return 0
        if grid[r][c] == 0: return 0
        if (r,c) in visit: return 0
        
        visit.add((r,c))
        
        left = dfs(r, c-1)
        right = dfs(r, c+1)
        top = dfs(r-1, c)
        down = dfs(r+1, c)
        
        return 1 + left + right + top + down 
    
    area = 0
    for r in range(m):
        for c in range(n):
            area = max(dfs(r, c), area)
    
    return area
            
            
            