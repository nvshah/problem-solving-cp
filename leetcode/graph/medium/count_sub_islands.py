# https://leetcode.com/problems/count-sub-islands/
from typing import List


def countSubIslands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    ''' DFS Search Approach '''
    visited = set()  # To check if islannd pertaining block is alreadu accounted or not 
    ROWS, COLS = len(grid1), len(grid1[0])

    def dfs(r, c):
        ''' Check if grid2 is possible sub island of grid1 (having pos[i,j])'''
        
        # 1. Boundaries | Water | Visited
        if r<0 or c<0 or r==ROWS or c==COLS or (grid2[r][c] == 0) or (r, c) in visited:
            return True 
        # Mark loc (i,j) as visited
        visited.add((r,c))

        #! We need to worry only when there is block which is part of Island
        # 3. Island (ie grid2[i][j] == 1)
        # Check corresp island block in Grid-1
        isSubIsland = grid1[r][c] == 1

        # Check for Neighbors (Need to Explore Island in Grid2 as well)
        isSubIsland = dfs(r+1, c) and isSubIsland # Bottom
        isSubIsland = dfs(r, c-1) and isSubIsland # Left 
        isSubIsland = dfs(r-1, c) and isSubIsland # Top
        isSubIsland = dfs(r, c+1) and isSubIsland # Right
            
        return isSubIsland

    count = 0
    for i in range(ROWS):
        for j in range(COLS):
            if grid2[i][j] == 1 and ((i,j) not in visited) and dfs(i, j):
                count += 1
    return count


# def countSubIslands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
#     ''' DFS Search Approach '''
#     visited = set()  # To check if islannd pertaining block is alreadu accounted or not 
#     ROWS, COLS = len(grid1), len(grid1[0])

#     def dfs(r, c, markOnly=False):
#         ''' Check if grid2 is possible sub island of grid1 (having pos[i,j])'''
        
#         # 1. Boundaries
#         if r<0 or c<0 or r==ROWS or c==COLS:
#             return True 
#         # 1.1 Visited earlier
#         if f'{r}{c}' in visited: return True
#         # Mark loc (i,j) as visited
#         visited.append(f'{r}{c}')

#         check = not markOnly
#         if check:
#             # 2. Water
#             if grid2[r][c] == '0':
#                 return True 

#             #! We need to worry only when there is block which is part of Island
#             # 3. Island (ie grid2[i][j] == '1')
#             # Check corresp island block in Grid-1
#             isSubIsland = grid1[r][c] == '1'

#         for x, y in [(r-1,c), (r,c+1), (r+1,c), (r,c-1)]:
#             isSubIsland = dfs(r+1, c, not isSubIsland) and isSubIsland # Bottom

#         # Check for Neighbors (Need to Explore Island in Grid2 as well)
#         isSubIsland = dfs(r+1, c, not isSubIsland) and isSubIsland # Bottom
#         isSubIsland = dfs(r, c-1, not isSubIsland) and isSubIsland # Left 
#         isSubIsland = dfs(r-1, c, isSubIsland) and isSubIsland # Top
#         isSubIsland = dfs(r, c+1, isSubIsland) and isSubIsland # Right
            
#         return isSubIsland

#     count = 0
#     for i in range(ROWS):
#         for j in range(COLS):
#             if grid2[i][j] == '1' and (f'{i}{j}' not in visited) and dfs(i, j):
#                 count += 1
#     return count
                
        
