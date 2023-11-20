# https://leetcode.com/problems/last-stone-weight-ii/
from math import ceil
from typing import List

'''
Idea -> Divide stones into 2 piles S.T. there is minimal diff between 2 piles weight
'''

def lastStoneWeightII(stones: List[int]) -> int:
    '''Include | Exclude (Memoization)'''
    totalSum = sum(stones)
    targetPile1 = ceil(totalSum / 2)

    cache = {} # (i, total)  i -> index, sum -> sum till index
    N = len(stones)

    def dfs(i, total):
        '''
        Find most suitable weight for pile1
        i -> stones to be accounted for pile1 onwards from ith index
        total -> total stones loaded in pile 1
        return minimal diff between 2 piles 
        '''
        if i == N or total >= targetPile1:
            pile1 = total 
            pile2 = totalSum - total 
            diff = abs(pile1 - pile2)
            return diff 

        if (i, total) in cache: 
            return cache[(i, total)] 
        
        d1 = dfs(i+1, total+stones[i]) # include
        d2 = dfs(i+1, total) # exclude

        cache[(i, total)] = v = min(d1, d2)
        return v 
    
    return dfs(0, 0) 

def lastStoneWeightII2(stones: List[int]) -> int:
    '''DP - Tabulation'''
    totalSum = sum(stones)
    target = ceil(totalSum / 2)

    stones.sort()
    N = len(stones)
    dp = [[0]*(target+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, target+1):
            if stones[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], stones[i-1] + dp[i-1][j - stones[i-1]])

    pile1 = dp[N][target]
    pile2 = totalSum - pile1

    return abs(pile1-pile2)
    

#stones = [2,7,1,4,8,1]  # 1
#a = [31,26,33,21,40]
#stones = [1,1,2,3,5,8,13,21,34,55,89,14,23,37,61,98] # 1
#stones = [34,30,6,25,13,32]  # 0
#stones = [2, 5, 6] 
ans = lastStoneWeightII2(stones)
print(ans)