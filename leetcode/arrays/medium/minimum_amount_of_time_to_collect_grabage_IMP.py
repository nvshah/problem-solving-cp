# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/
from typing import List 
from itertools import accumulate
from collections import Counter

'''
Idea: 
All the type of garbage at the end needs to be accounted
Hence at the end 
ans = Garbage-Count + TravelCount
Now
Garbage-Count From all houses is = count of garbage from all houses
TravelCount = Travel Truck to Last House having Corresp GarbageType
'''

def garbageCollection(garbage: List[str], travel: List[int]) -> int:
    lastHouse = {} # GarbageType -> HouseIdx
    totalGarbage = 0 
    totalTravel = 0

    for i, trash in enumerate(garbage):
        totalGarbage += len(trash)
        for category in trash:
            lastHouse[category] = i

    travelSum = [*accumulate(travel)] # i -> total cost to travel from (0 to i+1) house

    for i in lastHouse.values():
        if i > 0: # travel needed for collecting garbage of type {c}
            totalTravel += travelSum[i-1] # for {i} house travelTime is stored at i-1 pos in travelSum
    
    return totalGarbage + totalTravel



    

