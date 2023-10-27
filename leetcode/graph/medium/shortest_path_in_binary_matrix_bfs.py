# https://leetcode.com/problems/shortest-path-in-binary-matrix/
from typing import List
from collections import deque

'''
Idea : 
As we need to find shortest distance, we will use BFS
So going layer by layer next, we will assure asa we find the target it would be the
Shortest Distance (ie Greedy Search)

'''

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

def shortestPathBinaryMatrix2(grid: List[List[int]]) -> int:
    N = len(grid)  # Square is N*N

    if grid[N-1][N-1] != 0: return -1

    q = deque([(0, 0, 1)]) # (row, col, length)  // length to reach (r,c) from (0,0)
    visit = {(0,0)}  # visited cell per each level in BFS
    
    directions = [(-1, 0), (-1, +1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]  # directions
    
    while q:
        
        r, c, length = q.popleft()

        print('For ', r, c)

        if r == c == N-1:  # reach target
            print(r, c)
            return length 
        
        if (min(r, c) < 0 or  # boundary left
           max(r, c) >= N or  # boundary right
           grid[r][c]):       # Constraint
            continue

        for dx, dy in directions:
            dr, dc = r+dx, c+dy
            if (dr, dc) not in visit:
                q.append((dr, dc, length+1))
                visit.add((dr, dc))

    return -1

grid = [[0,0,0],[1,1,0],[1,1,1]]
ans = shortestPathBinaryMatrix2(grid)