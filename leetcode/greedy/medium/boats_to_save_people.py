# https://leetcode.com/problems/boats-to-save-people/
from typing import List

'''
QUe
You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

'''

def numRescueBoats(people: List[int], limit: int) -> int:
    ''' idea : Greedy Way
               Try to fill each boat in such a way that it has maximum weight near to limit as possible
                - For this you can try placing 1 heavy & 1 light person on boat as priority
                  & 
                  You can achieve this via Sort + 2 Pointer Technique
    '''
    # 1. sort the arr so that you can get light & heavy weight at same time (ie O(n*log(n)))
    people.sort()

    boats = 0  # total boats required (optimally)

    # 2. Pick light & heavy weight (greedily) each time to fill the boats
    l, r = 0, len(people)-1
    while l <= r:
        # pick a new boat
        boats += 1
        # add the heavy person first to boat
        remain, r = limit-people[r], r-1
        # still there are light weight person left (to enter the boat)
        if l <= r and people[l] <= remain:
            # try to add the light person to same boat
            l += 1 
    
    return boats
    
            
