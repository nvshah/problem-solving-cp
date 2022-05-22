# https://leetcode.com/problems/shortest-path-in-binary-matrix/
from typing import List
from collections import deque

def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    if grid[0][0] != 0: return -1
    q = deque([(0, 0, 1)]) # (row, col, cnt)
    visit = {(0,0)}  # visited cell per each level in BFS
    
    dir = [(-1, 0), (-1, +1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # directions
    
    while q:
        for i in range(len(q)):
            x, y, c = q.popleft()
            
            if x == m-1 and y == n-1: return c  # reach end (bottom-right)
            
            for i, j in dir:
                ni, nj = i+x, j+y
                if ni < 0 or ni == m or nj < 0 or nj == n: continue # boundaries
                if grid[ni][nj] == 1: continue # invalid path
                if (ni, nj) in visit: continue  # visited earlier (in earlier Level)
                
                # visit possible path cell
                visit.add((ni, nj))
                q.append((ni, nj, c+1))
    return -1