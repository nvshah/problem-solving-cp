# https://leetcode.com/problems/coin-change/

from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    ''' 
    idea :- DP - Bottom Up :- Go Column by Column in Tabular Form
    '''
    #! Suppply of Coin is infinite

    # dp Array Keep track for index {i = amount} -> min coins required 
    dp = [amount + 1] * (amount+1)
    dp[0] = 0 # To get amount {0} we do not need any coins

    coins.sort()  # ignore this if coins is already sorted
    for a in range(1, amount+1):
        for c in coins:
            ra = a-c   # remaining amount
            if ra < 0: # remaining amount cannot be satisifed
                break
            dp[a] = min(dp[a], 1 + dp[ra])  # 1 for curr coin {c} inclusion & rest for {ra} amount
    
    return dp[amount] if dp[amount] != amount+1 else -1

coins = [1,2,5]
amount = 11

coins = [2]
amount = 3

coins = [1]
amount = 0
nCoins = coinChange(coins, amount)
print(nCoins)



