# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

from typing import List

import itertools as it


def longestIncreasingPath(matrix: List[List[int]]) -> int:
    r,c = len(matrix), len(matrix[0])
    dp = [[0]*c for _ in range(r)]    # initially none of them are explored

    directions = [(0,1), (1,0), (0,-1), (-1,0)] # top, right, bottom, left

    def dfs(i, j): 
        ''' Search the Longest Increasing path from given index of cell i, j '''
        if dp[i][j]: return     # computed earlier

        v = matrix[i][j] 
        lip = 1                 # max possible length is cell itself

        for x, y in directions:
            ni, nj = i+x, j+y   # neighbour's cell location (ci,cj)
            if 0 <= ni < r and 0 <= nj < c:  # if cell is inbounded
                neigh = matrix[ni][nj]
                if v < neigh:         # if can move to {neighbour} via `+1` step
                    dfs(ni, nj)          # explore reachability of {neighbour}
                    nr = 1 + dp[ni][nj]  # reach to {neighbour}
                    lip = max(lip, nr)   # update local LIP for curr cell (i,j)
                    
        dp[i][j] = lip  # cache founded LIP for curr cell (i,j)

    # for i in range(r):
    #     for j in range(c):
    #         dfs(i, j)

    for i, j in it.product(range(r), range(c)):
        dfs(i, j)
        
    return max(it.chain.from_iterable(dp))

matrix = [[9,9,4],[6,6,8],[2,1,1]]
lip = longestIncreasingPath(matrix)
print(lip)


