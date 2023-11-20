# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles
from typing import List

def maxValueOfCoins(piles: List[List[int]], k: int) -> int:
    '''Top-Down Memoization'''
    N = len(piles)
    dp = [[-1]*(k+1) for _ in range(N)]

    def dfs(i, coins):
        '''current pile at [i] with [coins] yet left to be picked'''
        if i == N: return 0 # exhausted all piles (no pile = no coin)
        if coins == 0: return 0 # no coins left to be picked so cant add any value
        
        if dp[i][coins] != -1:
            return dp[i][coins]

        value = dfs(i+1, coins) # skip current pile

        pile = piles[i]
        toPick = min(len(pile), coins)
        curAmt = 0

        # account current pile
        for j in range(toPick):
            curAmt += pile[j]
            rest = dfs(i+1, coins-j-1) # account (j+1) coin from cur-pile 
            value = max(value, curAmt + rest)
        
        dp[i][coins] = value
        return value 
    
    return dfs(0, k) # first pile & k-coins yet to be selected

def maxValueOfCoins2(piles: List[List[int]], k: int) -> int:
    '''DP - TLE (Not passed all cases)'''
    N = len(piles)
    dp = [0]*(k+1)

    for i in range(N-1, -1, -1): # piles
        pile = piles[i]
        newDp = list(dp)
        limit = len(pile)

        for coins in range(1, k+1): # coins
            val = dp[coins] # best val for pile-i & coins allowed to pick
            curAmt = 0
            for j in range(1, coins+1): # try diff combination with current pile
                if j <= limit:
                    curAmt += pile[j-1] # pick first j from cur-pile & rest from others
                val = max(val, curAmt + dp[coins-j])
            newDp[j] = val
        
        dp = newDp

    return dp[k]

# TEst ------
piles, k = [[1,100,3],[7,8,9]], 2
#piles, k = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], 7
ans = maxValueOfCoins2(piles, k)
print(ans)