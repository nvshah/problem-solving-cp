# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List

def maxProfit(prices: List[int]) -> int:
    N = len(prices)
    profit = 0
    buyDay = 0  # window -> [buy, sell]

    for sellDay in range(1, N):
        if prices[buyDay] < prices[sellDay]:
            # profitable
            profit = max(profit, prices[sellDay]-prices[buyDay])
        else:
           buyDay = sellDay
    
    return profit 