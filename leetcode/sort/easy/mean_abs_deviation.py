# https://leetcode.com/problems/minimum-absolute-difference/

from typing import List
import itertools as it
import sys


def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    size, ans = len(arr), []
    arr.sort()
    d = arr[1] - arr[0] # first pair diff
    i = 2
    ans.append([arr[0], arr[1]]) # assume first pair diff is smallest at start
    while i < size:
        t = arr[i] - arr[i-1]
        if t <= d:
            if t < d:  # new small difference found
                d = t
                ans.clear() # remove previous founded pairs
            ans.append([arr[i-1], arr[i]])
        i+=1
    return ans

minimumAbsDifference([1,3,6,10,15])
minimumAbsDifference([4, 2, 1, 3])
minimumAbsDifference([3,8,-10,23,19,-4,-14,27])






