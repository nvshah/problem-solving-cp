# https://leetcode.com/problems/maximum-performance-of-a-team/
import heapq
from typing import List

'''
Idea1 :- Brute Force (Decision Binary Tree)
         T.C := 2^n (ie Exponential)

         Where each path from root to leaf will be eligible candidate (having group of engineers)
         in list
         Thus here candidates of groups are in high number as each path = single group = candidate

Idea2 :- Sliding Window by finding each group keeping in mind the current candidate Efficiency
         (ie based on selected candidate efficiency pick other candidates in group)
         This way we will reduce the candidates of groups

         This is possible because we know that In each group Candidate with min-efficiency would be
         considered as captain 
'''

def maxPerformance(n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    '''T.C := nlogn + nlogk'''
    # 1. Sort according to Efficiecny in reverse order
    engineers = sorted(zip(efficiency, speed), reverse=True)

    # minHeap of speeds of current group of engineer (ie candidates)
    group = [] # min-heap
    best = 0  # maxPerformance
    tSpeed = 0  # total speed of current grp

    # 2 Try to find ideal group for each engineer
    for eff, spd in engineers:
        # 2.1 check if group is not full
        if len(group) == k:  # i.e Window exceeded
            # remove the engineer with lowest speed (so that performance remains highest after considering [spd] & [eff])
            tSpeed -= heapq.heappop(group)
        # Account current engineer (ie [eff], [spd])
        heapq.heappush(group, spd)  # include in current group
        tSpeed += spd
        best = max(best, eff*tSpeed)

    return best % (10**9 + 7)



