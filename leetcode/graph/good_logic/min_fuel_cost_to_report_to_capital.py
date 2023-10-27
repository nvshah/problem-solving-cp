# https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
from typing import List
from collections import defaultdict
from math import ceil

# DFS

# O(n) time 
def minimumFuelCost(roads: List[List[int]], seats: int) -> int:
    # prepare adjacency matrix (undirected graph)
    adjMatrix = defaultdict(list)
    for i, j in roads:
        adjMatrix[i].append(j)
        adjMatrix[j].append(i) 
    
    # start exploring from capital city (ie 0) towards all other cities
    cost = 0
    def dfs(node, parent):
        '''
        Find total passengers travelling to [parent] from [node]
        1. find total passengers arriving to [node] & their respective fuel costs
        2. return total passengers travelling to [parent]
        '''
        nonlocal cost
        arrivingPassengers = 0 # total visitors to [node]
        for child in adjMatrix[node]:
            if child != parent:
                travellers = dfs(child, node) # passengers arriving to [node] from [child]
                # compute the travel cost of [child] -> [node] = #cars-needed 
                carsRequired = ceil(travellers/seats)
                cost += carsRequired # ie 1 fuel per car

                arrivingPassengers += travellers # accumulate the arriving passengers

        # depart towards [parent]
        departingPassengers = arrivingPassengers + 1 # 1 for [node] itself 
        return departingPassengers
    
    dfs(0, -1) # start from capital city
    return cost

# O(n) time 
def minimumFuelCost2(roads: List[List[int]], seats: int) -> int:
    # prepare adjacency matrix (undirected graph)
    adjMatrix = defaultdict(list)
    for i, j in roads:
        adjMatrix[i].append(j)
        adjMatrix[j].append(i) 
    
    # start exploring from capital city (ie 0) towards all other cities
    def dfs(node, parent):
        '''
        return (totalPax, spentCost) 
        - totalPax: total passengers gathered at [node] (including itself)
        - spentCost: cost of travel of [totalPax] from [node] -> [parent]
        '''
        arrivingPax = 0 # total visitors to [node]
        arrivingCosts = 0
        for child in adjMatrix[node]:
            if child != parent:
                travellers, cost = dfs(child, node) # passengers arriving to [node] from [child]
                arrivingCosts += cost
                arrivingPax += travellers # accumulate the arriving passengers

        departingPax = arrivingPax + 1 # 1 for [node] itself     
        departingCars = 0
        if parent != -1:
            # depart towards [parent]
            departingCars = ceil(departingPax / seats) # For departure from [node] -> [parent]

        totalCosts = departingCars + arrivingCosts
        return departingPax, totalCosts
    
    _, cost = dfs(0, -1) # start from capital city
    return cost

roads = [[0,1],[0,2],[0,3]]