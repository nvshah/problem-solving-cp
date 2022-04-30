
from typing import List
import bisect
from operator import itemgetter

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
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


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    li = bisect.bisect(intervals, newInterval[0], key=itemgetter(0))
    ri = bisect.bisect(intervals, newInterval[1], key=itemgetter(1))

    if li == 0:
        n = intervals[i+1]
        if newInterval[1] >= n[0]:
            # merge 
            intervals.insert(i, [newInterval[0], n[1]])
            del intervals[i+1]
        else:
            intervals.insert(i, newInterval)

    elif i == len(intervals):
        p = intervals[i-1]
        if newInterval[0] <= p[1]:
            # merge 
            intervals.insert(i, [p[0], newInterval[1]])
            del intervals[i-1]
        
        else:
            intervals.insert(i, newInterval)
    else: 
        n = intervals[i+1]
        p = intervals[i-1]
        t = newInterval
        r = []
        if n[0] <= t[1]:
            t[1] = n[1]
            r.append(i+1)
        if p[1] >= t[0]:
            t[0] = p[0]
            r.append(i-1)
        
        intervals.insert(i, t)
        for j in r:
            del intervals[j]

    print(intervals)


intervals = [[1,3],[6,9]]
newInterval = [2,5]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
#newInterval = [0,8]

insert(intervals, newInterval)