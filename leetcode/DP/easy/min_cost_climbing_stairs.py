# https://leetcode.com/problems/min-cost-climbing-stairs/

'''
QUE

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. 
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
'''

from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    # Start from Right Side -> Left Side
    f, s = cost[-1], 0  # last second, last
    
    for c in cost[-2::-1]:
        f, s = min(c+f, c+s), f
        
    return min(f, s)
        