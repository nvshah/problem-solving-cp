# https://leetcode.com/problems/counting-bits/
from typing import List 

def countBits1(n: int) -> List[int]:
    # via builtin function
    return [i.bit_count() for i in range(n+1)]
    
def countBits2(n: int) -> List[int]:
    # via DP -----------
    dp = [0]*(n+1)  # ans
    o = 1 # offset is in power of 2
    
    for i in range(1, n+1):
        if i == 2*o:
            o = i
        dp[i] = 1 + dp[i-o]
    
    return dp