# https://leetcode.com/problems/number-of-provinces/
from typing import List

def findCircleNum(isConnected: List[List[int]]) -> int:
    n = len(isConnected) # city counts
    # initially all cities are province (assumption)
    provinces = [i for i in range(n)]  
    # cityCnts[i] = number of cities that are part of that province where {i} is the capital|firstCity
    cityCnts = [1]*n  # cityCnts[i] will be non-zero if i is capital else it will be 0

    def find(city):
        '''find the capital city of province where {city} belongs'''
        c = city   # every {city} is atleast {province} in itself
        
        # 1. find the capital
        while c != provinces[c]:
            c = provinces[c]
            
        # Now {c} is the capital of provice where {city} belongs -------
        
        # 2. Path Compression for all city of that province
        while city != c: 
            provinces[city], city = c, provinces[city]

        return c

    def union(c1, c2):
        '''
        c1 & c2 are 2 cities which are connected to each other
        Aim :- Extend either province if require to acclimate both the cities {c1} & {c2}
                - Extending means merge 1 province into another if required
        
        return 1 if new Province is formed by Merge
                0 if cities {C1}, {c2} already belong to same province
        '''
        # find capital(first city of province) for both the cities {c1} & {c2}
        f1, f2 = find(c1), find(c2) 

        if f1 == f2:  # both of them already belong to same province
            return 0

        # need to merge either province
        if cityCnts[f1] >= cityCnts[f2]:
            # province with capital={f1} has more or equal cities, so include all cities from f2's province into it
            provinces[f2] = f1
            cityCnts[f1] += cityCnts[f2]  # add all cities of {f2} -> {f1}
            cityCnts[f2] = 0  # update cityCnts of {f2} as {f2} is no longer capital
        else:
            # province with capital={f2} has more cities, so include all cities from f1's province into it
            provinces[f1] = f2
            cityCnts[f2] += cityCnts[f1] # add all cities of {f1} -> {f2}
            cityCnts[f1] = 0  # update cityCnts of {f1} as {f1} is no longer capital

        return 1  # new province formed

    # initially all cities are individual province
    total = n   # total provices count
    for i in range(n):
        for j in range(n):
            if isConnected[i][j]:
                total -= union(i, j)

    return total