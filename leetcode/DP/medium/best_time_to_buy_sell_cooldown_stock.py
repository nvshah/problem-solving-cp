# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
from typing import List

def maxProfit (prices: List[int]) -> int:
    # State -> True/False
    # buy := (True) if you can buy stock at given {i}
    # sell := (False) you can sell stock at given {i}
    cache = {} # dp -> (i, canBuy)
    sz = len(prices)
    def dfs(i, canBuy):
        '''return max profit from idx {i}'''
        if i == sz: return 0
        k = (i, canBuy)
        if k in cache: return cache[(i, canBuy)]

        cooldown = dfs(i+1, canBuy) # move to next idx as it is
        if canBuy:
            bought = -prices[i] + dfs(i+1, False)
            cache[k] = max(bought, cooldown)
        else: # can Sell
            sold = prices[i] + dfs(i+2, True) # if sold then compulsory need 1 day of cooldown before next buy so used {i+2}
            cache[k] = max(sold, cooldown)
        
        return cache[k]
    
    return dfs(0, True)


