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

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-10]]
print(minimumTotal(triangle))