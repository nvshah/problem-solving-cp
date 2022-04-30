# https://leetcode.com/problems/koko-eating-bananas/

from typing import List

from math import ceil


def minEatingSpeed(piles: List[int], h: int) -> int:
    minSpeed = 1 
    maxSpeed = max(piles)  # koko can eat maximumn bananas in single hour = largest piles

    def findTime(rate):
        ''' 
        Find the time to eat all bananas at given rate
        '''
        time = 0
        return sum([ceil(cnt/rate) for cnt in piles])

    s, e = minSpeed, maxSpeed
    k = 0  # optimal rate
    while s <= e:
        rate = (s+e)//2
        t = findTime(rate)
        if t > h: # Takes more than h hours at {rate}
            # So increase rate
            s = rate + 1
        else:
            k = rate 
            # Greedy try to find for lesser rate
            e = rate-1
    return k