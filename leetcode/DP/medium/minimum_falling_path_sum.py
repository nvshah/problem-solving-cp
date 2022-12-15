# https://leetcode.com/problems/minimum-falling-path-sum/solutions/
from typing import List

def minFallingPathSum(A: List[List[int]]) -> int:
    m, n = len(A), len(A[0])
    # We will use A as only the DP (Matrix) Cache
    for i in range(1, m):  # start from 2nd row
        for j in range(n):
            top_left = A[i - 1][j - 1] if 0 <= j - 1 else float('inf')
            top = A[i - 1][j]
            top_right = A[i - 1][j + 1] if j + 1 < n else float('inf')
            A[i][j] += min(top_left, top, top_right)
    return min(A[m - 1])  # Min from last row

