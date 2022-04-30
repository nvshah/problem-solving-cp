# https://leetcode.com/problems/pacific-atlantic-water-flow/
from typing import List

'''
idea :- We will try to do reverse Lookup from both the end (ie Atlantic & Pacific)
        To see what is reachability from both the end !!

        Reachability 
          - from cell -> Ocean End :- must be in decreasing order
        whereas 
        In case of Reverse Lookup (ie)
          - From Ocean End -> Cell :- must be in increasing order (ie Opposite)

        So we will perform Reverse Lookup for Reachibility via DFS
'''

def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    '''
    IDEA :- Reverse Reachability Lookup via DFS
    '''
    m, n = len(heights), len(heights[0])
    # keep tracks of visited cells from respective Ocean ends (in Reverse Reachability Lookup)
    pac, atl = set(), set()

    def dfs(r, c, visited, prevHeight):
        '''
        :param r: row number
        :param c: col number
        :param visited: set of visisted cells
        :param prevHeight: prevCell Height 
        '''
        # 1. Check if cell is in bounds
        if r < 0 or r == m or c < 0 or c == n:
            return 
        
        # 2. Check if Visited
        if (r,c) in visited:
            return

        # 3. Check Constraint for Reverse lookup (ie Increasing order)
        height = heights[r][c]
        if height < prevHeight:
            return 
        
        # 4. Make current cell as Visited (ie valid cell for reachability by respective Ocean End)
        visited.add((r,c))

        # 5. Explore further Reachibility (ie via Neighbors)
        dfs(r-1, c, visited, height)
        dfs(r, c+1, visited, height)
        dfs(r+1, c, visited, height)
        dfs(r, c-1, visited, height)


    # 1. Row Ends from Both (Pacific & Atlanntic) 
    #    NOTE : First Row is Reachable to Pacific Ocean (automatically)
    #           & Likewise, Last Row is Reachable to Atlantic Ocean (automatically)
    for c in range(n):
        dfs(0, c, pac, -1) # for Pacific Ocean
        dfs(m-1, c, atl, -1) # for Atlantic Ocean

    # 2. Col Ends from Both (Pacific & Atlanntic) 
    #    NOTE : First Col is Reachable to Pacific Ocean (automatically)
    #           & Likewise, Last Col is Reachable to Atlantic Ocean (automatically)

    for r in range(m):
        dfs(r, 0, pac, -1) # for Pacific Ocean
        dfs(r, n-1, atl, -1) # for Atlantic Ocean

    # 3. Common Cells
    common = pac & atl 
    return common
    
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
ans = pacificAtlantic(heights)
print(ans)
