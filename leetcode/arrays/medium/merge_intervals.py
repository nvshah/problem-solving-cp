# https://leetcode.com/problems/merge-intervals/
from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    cur = intervals[0]
    res = [cur]

    for nxt in intervals[1:]:
        if cur[1] >= nxt[0]: # overlapping
            cur[1] = max(cur[1], nxt[1]) # update cur-end
        else: # new Interval
            res.append(nxt)
            cur = nxt 
             
    return res 