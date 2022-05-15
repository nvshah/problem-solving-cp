# https://leetcode.com/problems/remove-covered-intervals/
from typing import List

'''
QUE
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.
'''

def removeCoveredIntervals(intervals: List[List[int]]) -> int:
    # sort s.t interval with small start val comes first &
    # on Tie interval with bigger end val gets priority
    intervals.sort(key=lambda x: (x[0], -x[1]))

    res = [intervals[0]] # remain intervals

    for l, r in intervals[1:]:
        prevL, prevR = res[-1]
        
        if prevL <= l and r <= prevR: 
            continue # contained in prev interval
        res.append((l, r))
    
    return len(res)

intervals = [[1,4],[3,6],[2,8]]
ans = removeCoveredIntervals(intervals)
print(ans)