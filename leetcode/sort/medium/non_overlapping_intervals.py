# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals.sort()
    cnt = 0

    prevEnd = intervals[0][1]
    for s, e in intervals[1:]:
        if s >= prevEnd:
            prevEnd = e
        else :
            cnt += 1
            prevEnd = min(prevEnd, e)
            
    return cnt

intervals = [[1,2],[1,2],[1,2]]
#intervals = [[1,2],[2,3]]

#intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [[1,2], [2,4], [2,3], [1,4], [3,4], [4,5]]
a = eraseOverlapIntervals(intervals)
print(a)

                

