# https://leetcode.com/problems/insert-interval/discuss/1800292/python-solution-simple-traversal-on-comments

from typing import List
import bisect
from operator import itemgetter

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    ''' O(n) ''' 
    res = []
    nl, nu = newInterval  # new lower & new upper bounds
    for i, interval in enumerate(intervals):
        cl, cu = interval  # current lower & current upper bounds
        if nu < cl:  # before current interval {i}
            res.append(newInterval)
            return res + intervals[i:]
        if nl > cu:  # after current interval {i}
            res.append(interval)
        else: # Overlapping with Current Interval {i}
            newInterval = nl, nu = min(nl, cl), max(nu, cu)
            # Note Here we are not adding this new Interval as it may overlap with future intervals as well

    res.append(newInterval)   # need to add eventually to result
    return res