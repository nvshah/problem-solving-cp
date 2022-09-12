class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        size = len(prices)
        
        @cache
        def helper(i: int, profit: int, k: int, holding : bool) -> int:
            if (k == -1) or (i == size):
                return profit
            
            if (holding):
                return max(
                    # If we sell the holding stock, profit would be changed
                    helper(i + 1, profit + prices[i], k, False),
                    
                    # If we don't sell the holding stock, keep the current profit
                    helper(i + 1, profit, k, True)
                )
            else:
                return max(
                    # If we buy the stock[i], profit decrease
                    helper(i + 1, profit - prices[i], k - 1, True),
                    
                    # If we don't buy the stock[i], keep the current profit
                    helper(i + 1, profit, k, False)
                )
        return helper(0, 0, k, False)


# ----

# -> Bottom Up
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        size = len(prices)
        
        @cache
        def helper(i: int, k: int, holding : bool) -> int:
            if (k == -1) or (i == size):
                return 0
			
			# keep the current situation
            doNothing = helper(i + 1, k, holding)
            
            if (holding):
                return max(
                    # If we sell the holding stock, profit would be changed
                    helper(i + 1, k, False) + prices[i],
                    
                    doNothing
                )
            else:
                return max(
                    # If we buy the stock[i], profit decrease
                    helper(i + 1, k - 1, True) - prices[i],
                    
                    doNothing
                )
        return helper(0, k, False)

# -----
