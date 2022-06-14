    # https://leetcode.com/problems/triangle/

from typing import List 

def minimumTotal(triangle: List[List[int]]) -> int:
    ''' Idea :- start from bottom (base) & find min path sum level wise likewise'''
    # dp -> base to current level in triangle
    dp = [0]*(len(triangle)+1)

    for t in triangle[::-1]:
        for i, e in enumerate(t):
            # child for {i} -> dp[i], dp[i+1]
            dp[i] = e + min(dp[i], dp[i+1]) # Find min path from child lying on base {dp}

    return dp[0] # for root -> first

def minimumTotal2(triangle: List[List[int]]) -> int:
    l = len(triangle)
    dp = triangle[l-1]
    for i in range(l-2, -1, -1):
        for j in range(i+1):
            v = triangle[i][j]    # curr value at curr layer
            l, r = dp[j], dp[j+1] # left, right on below layer
            dp[j] = v + min(l, r)
    
    return dp[0]


triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-10]]
print(minimumTotal(triangle))