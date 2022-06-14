# https://leetcode.com/problems/triangle

from typing import List


def minimumTotal(triangle: List[List[int]]) -> int:
    l = len(triangle)
    dp = triangle[l-1]
    for i in range(l-2, -1, -1):
        for j in range(i+1):
            v = triangle[i][j]    # curr value at curr layer
            l, r = dp[j], dp[j+1] # left, right on below layer
            dp[j] = v + min(l, r)
    
    return dp[0]

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
minimumTotal(triangle)