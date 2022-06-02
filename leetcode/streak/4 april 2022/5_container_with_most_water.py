# https://leetcode.com/problems/container-with-most-water/
from typing import List 

'''
QUE

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.

'''

def maxArea2(height: List[int]) -> int:
    ''' Optimal Soln :- Quick Search (2 Pointers) | O(n) '''
    res = 0
    n = len(height)
    l, r = 0, n-1
    while l < r:
        hl, hr = height[l], height[r]
        area = (r-l)*min(hl,hr)
        res = max(res, area)

        if hl < hr:
            l += 1
        else:
            r -= 1
    
    return res



# Just for Undnerstanding
def maxArea1(height: List[int]) -> int:
    ''' Brute Force Approach O(n^2) '''
    res = 0
    n = len(height)
    for l in range(n):
        h1 = height[l]
        for r in range(l+1, n):
            area = (r-l) * min(h1, height[r])
            res = max(res, area)
    return res

