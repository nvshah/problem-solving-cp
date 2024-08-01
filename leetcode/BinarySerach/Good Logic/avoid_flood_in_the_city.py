# https://leetcode.com/problems/avoid-flood-in-the-city
from typing import List 
from sortedcontainers import SortedList 
import bisect

'''
Greedy | Bisect | BinarySearch

Greedy approach: empty the lake when needed

Use sorted array & binary search to discover which day is available to empty nth lake (S.T. day > n)

T.C := O(nlogn)
S.C := O(n)
'''
# ----- Newer Approach -----------

def find_gt(a, x):
    'Find value higher than & closest to x'
    i = a.bisect_right(x)
    if i != len(a):
        return a[i]
    return None 

def avoidFlood(rains: List[int]) -> List[int]:
    fullLakes = {}
    dryDays = SortedList()
    res = [-1]*len(rains)

    for day, lake in enumerate(rains):
        if lake == 0:
            dryDays.add(day)
            res[day] = 1  # by default select first lake to empty
        else:
            if lake in fullLakes:
                # Empty it
                dayOfFull = fullLakes[lake]
                dryDay = find_gt(dryDays, dayOfFull)
                if dryDay is None: return [] # cannot avoid Flood
                dryDays.remove(dryDay)
                res[dryDay] = lake

            fullLakes[lake] = day 

    return res 

# -------- Older Approach -------

def find_gt(a, x):
    'Find value higher than & closest to x'
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    return None 

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        fullLakes = {}
        dryDays = []
        res = [-1]*len(rains)

        for day, lake in enumerate(rains):
            if lake == 0:
                dryDays.append(day)
                res[day] = 1  # by default select first lake to empty
            else:
                if lake in fullLakes:
                    # Empty it
                    dayOfFull = fullLakes[lake]
                    dryDay = find_gt(dryDays, dayOfFull)
                    if dryDay is None: return [] # cannot avoid Flood
                    dryDays.remove(dryDay)
                    res[dryDay] = lake

                fullLakes[lake] = day 

        return res 

rains = [1,2,3,4]
#rains = [1,2,0,0,2,1]
#rains = [1,2,0,1,2]
#rains = [0,1,1]
ans = avoidFlood(rains)
print(ans)


