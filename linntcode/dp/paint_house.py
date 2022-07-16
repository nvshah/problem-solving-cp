#https://www.lintcode.com/problem/515/

'''
QUE
There are a row of n houses, each house can be painted with one of the three colors: red, blue or green. 
The cost of painting each house with a certain color is different. 
You have to paint all the houses such that no two adjacent houses have the same color,
 and you need to cost the least. Return the minimum cost.

The cost of painting each house with a certain color is represented by a n x 3 cost matrix. 
For example, costs[0][0] is the cost of painting house 0 with color red; 
costs[1][2] is the cost of painting house 1 with color green, and so on... 
Find the minimum cost to paint all houses.

'''

from typing import List


def min_cost(costs: List[List[int]]) -> int:
    dp = costs[0]  # dp -> prev house cost (ie last row)

    for cost in costs[1:]:
        cost1 = cost[0] + (dp[1], dp[2])
        cost2 = cost[1] + (dp[0], dp[2])
        cost3 = cost[2] + (dp[0], dp[1]) 

        dp = [cost1, cost2, cost3]
    
    return min(dp)
        