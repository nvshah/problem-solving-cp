# https://leetcode.com/problems/minimum-path-sum/

from typing import List
from sys import maxsize


def minPathSum(grid: List[List[int]]) -> int:
    ''' DP -> Bottom UP Approach '''

    rows, cols = len(grid), len(grid[0])

    # Add extra 1 Row & 1 Column to avoid boundaries
    dp = [[maxsize]*(cols+1) for _ in range(rows+1)] 
    dp[rows-1][cols] = 0 # to make math work around

    for r in range(rows-1, -1, -1):
        for c in range(cols-1, -1, -1):
            dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])

    return dp[0][0]
