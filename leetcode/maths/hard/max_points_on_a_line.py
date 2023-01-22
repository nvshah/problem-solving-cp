# https://leetcode.com/problems/max-points-on-a-line/
from typing import List
from collections import defaultdict

'''
Given an array of points where points[i] = [xi, yi] 
represents a point on the X-Y plane, 
return the maximum number of points that lie on the same straight line.
'''

'''
SOLN
(IDEA)
Find the Slope between pair of Points to identify if point lies on same line or not

For each point we will find the possibilities of Slopes/Lines it belongs to
'''

def maxPoints(points: List[List[int]]) -> int:
    # NOTE: Slope helps us to idenitfy if multiple points lies on same line or not
    #       Slope is calc of a line (ie Pair of Points)
    #       Points lying on same line (ie Plane) will have same slope
    INF = float('inf')
    n = len(points)
    
    res = 1  # Atleast single point has its own Line Direction

    for i, (x1, y1) in enumerate(points[:-1]):
        # line/slope -> cnt  // point count for corresponding line/slope
        counts = defaultdict(int)

        # NOTE: Here we are checking upcoming points as previous points are already explored for lines/slopes in a Pair
        # Find all the lines/slopes where point (x1, y1) may belong to -> 
        for j in range(i+1, n):
            x2, y2 = points[j]
            # slope S.T. (x1,y1) & (x2,y2) lie on it
            slope = INF if x1==x2 else (y2-y1)/(x2-x1)
            # New Point found with line having {slope}
            counts[slope] += 1

        # Max points on line (when (x1, y1)) is included
        cnt = max(counts.values()) + 1  # +1 for (x1, y1) itself
        res = max(res, cnt) 
    
    return res

def maxPoints2(points: List[List[int]]) -> int:
    # NOTE: Slope helps us to idenitfy if multiple points lies on same line or not
    #       Slope is calc of a line (ie Pair of Points)
    #       Points lying on same line (ie Plane) will have same slope
    INF = float('inf')
    n = len(points)
    
    res = 1  # Atleast single point has its own Line Direction

    for i in range(n):
        x1, y1 = points[i] 
        # line/slope -> cnt  // point count for corresponding line/slope
        counts = defaultdict(int)

        # NOTE: Here we are checking upcoming points as previous points are already explored for lines/slopes in a Pair
        # Find all the lines/slopes where point (x1, y1) may belong to -> 
        for j in range(i+1, n):
            x2, y2 = points[j]
            # slope S.T. (x1,y1) & (x2,y2) lie on it
            slope = INF if x1==x2 else (y2-y1)/(x2-x1)
            # New Point found with line having {slope}
            counts[slope] += 1
            # when (x1, y1)) is included
            res = max(res, counts[slope]+1)
    
    return res

points = [[1,1],[2,2],[3,3]]
ans = maxPoints(points)

print(ans)
