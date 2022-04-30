# https://leetcode.com/problems/car-pooling/
from typing import List
from operator import itemgetter
import heapq

def carPooling1(trips: List[List[int]], capacity: int) -> bool:
    ''' O(nlogn) '''
    # 1. sort the trip according to start location
    trips.sort(itemgetter(1))

    # 2. minHeap -> according to end Date (ie nearby drop loc at top)
    minHeap = [(1001,-1)] # pair :- (end, #passengers)
    curCnt = 0 # current count of passengeer in Car

    # 3. attend each trip in row
    for t in trips:
        p, s, e = t  # passengers, start, end

        # check for trips that already ended till now
        while minHeap[0][0] <= s:
            _, n = heapq.heappop(minHeap)
            curCnt -= n

        # pick & add curr passengers {p} to Car
        curCnt += p 

        if curCnt > capacity:
            return False 
        
        # record the drop loc for all cur picked passengers {p}
        heapq.heappush(minHeap, (e, p)) 

    return True

def carPooling2(trips: List[List[int]], capacity: int) -> bool:
    ''' O(n) Given Constraints '''
    n = len(trips)
    # 1. Mark 1000 destinations with 0 passengers pickup earlier
    loc = [0]*1001  # locations

    # mark #passengers in car at each loaction (ie pick & drop both)
    for t in trips:
        n, s, e = t
        loc[s] += n  # picked
        loc[e] -= n  # dropped

    curCnt = 0  # curr passenger cnt in car
    for i in range(1001):
        curCnt += loc[i]
        if curCnt > capacity:
            return False 
    
    return True


def carPooling3(trips: List[List[int]], capacity: int) -> bool:
    ''' O(nlogn) '''
    # 1. create minheap based on start location to be picked
    pickups = [(s, e, n) for n, s, e in trips]  # pair :- (start, #passengers)
    heapq.heapify(pickups) # O(n)

    # 2. create minHeap based on end location to drop
    drops = [(1001, -1)]  # pair :- (end, #passengers)

    curCnt = 0 # curr passengers in car

    # till there are passengers to be picked
    while pickups:
        s, e, p = heapq.heappop(pickups)  # start, passengers

        # check for trips that already ended till now
        while drops[0][0] <= s:
            _, n = heapq.heappop(drops)
            curCnt -= n

        # pick & add curr passengers {p} to Car
        curCnt += p 

        if curCnt > capacity:
            return False 
        
        # record the drop loc for all cur picked passengers {p}
        heapq.heappush(drops, (e, p)) 

    return True

trips = [[2,1,5],[3,3,7]]
capacity = 4

trips = [[2,1,5],[3,3,7]]
capacity = 5

ans = carPooling3(trips, capacity)
print(ans)

