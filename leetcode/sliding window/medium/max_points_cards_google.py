# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

from typing import List

'''
Task :- select from either end {k} elements that total upto max Val
'''

def maxScore(cardPoints: List[int], k: int) -> int:
    '''
    Idea :- Sliding Window that will slide {k} times from starting
    '''
    size = len(cardPoints)
    l = 0    # point to first element of window
    r = size - k # points to next immediate element outside current window

    total = sum(cardPoints[r:])
    res = total # optimal total

    for _ in range(k):
        # If window moved 1 step in right direction
        # element by {l} will be eligible from left end & 
        # element by {r} will be ineligible from right side (as it gets included in window post Window movement by 1 step)
        total = total + cardPoints[l] - cardPoints[r]
        res = max(total, res)  # optimal

        l, r = l+1, r+1  # Shift the window by 1 ste

    return res 

cardPoints = [1,2,3,4,5,6,1]
k = 3

ans = maxScore(cardPoints, k)
print(ans)