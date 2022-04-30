# https://leetcode.com/problems/cheapest-flights-within-k-stops/
from typing import List

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    '''Idea :- BellMan-Ford Algo 
               (Layer by Layer alike BFS)
    '''
    inf = float("inf")
    prices = [inf]*n  # price to reach each vertices from start node {0}
    prices[src] = 0  # start node (ie src) := 0

    # end node (ie destination) := n-1

    # In order to reach the dst from src with atmost k stops we need (k+1) step-level search
    for i in range(k+1):
        tmpPrices = prices.copy()  # will hold the latest price for this step|layer

        # s := source, d := destination, p := flight's price
        for s, d, p in flights:
            # 1. check if source {s} can be reached now before moving to {d} from {s}
            if prices[s] == inf:
                continue  # as there is no flight to {s} as of now from start ie {src}
            
            # 2. check if {s} -> {d} is cheaper flight
            ps = prices[s] # price to reach {s} (from {src})
            pd = ps + p # price to d via route from {s} 
            # In cur step there can be multiple routes to {d} so considreing updated {tmpPrices} for destination
            tmpPrices[d] = min(pd, tmpPrices[d])

        # 3. update the cur prices to original one
        prices = tmpPrices
    
    # end node := {dst}
    return -1 if prices[dst] == inf else prices[dst]

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1  

ans = findCheapestPrice(n, flights, src, dst, k)
print(ans)






