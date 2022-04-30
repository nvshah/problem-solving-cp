# https://leetcode.com/problems/perfect-squares/

'''
This problem is same as Coin change
'''

from math import isqrt

def numSquares(n: int) -> int:
    '''
     T.C = O(n*sqrt(n))

     NOTE :- If we use Greedy Then me way not get minimal perfect-Squares
             To get minimal Perfect Squares we use DP approach
    '''
    # In worst case to get n = (1+1+1... n times)
    # dp keep tracks of minimal perfect squares number require for sum corresp to index
    dp = [n] * (n+1)
    dp[0] = 0  # to get 0 as sum we do not require any nummber

    # In tabular Form of DP -> we are traversing Column by Column
    for target in range(1, n+1):  # O(n)
        for n in range(1, isqrt(target)+1): # O(sqrt(target))
            sq = n * n 
            left = target - sq
            # if left < 0:  # no square further can fulfill the target 
            #     break
            # {sq} can be used ie look for {left} minimal coins onwards
            dp[target] = min(dp[target], 1 + dp[left])
    
    print(dp)
    
    return dp[n]

numSquares(13)

            

