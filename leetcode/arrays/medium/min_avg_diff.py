# https://leetcode.com/contest/biweekly-contest-77/problems/minimum-average-difference/
from typing import List 
from itertools import accumulate

def minimumAverageDifference(nums: List[int]) -> int:
    n = len(nums)
    left = list(accumulate(nums))
    right = [*[*accumulate(nums[:0:-1])][::-1], 0]

    def mad(i):
        f = left[i]//(i+1)
        s = right[i]//(max(n-i-1, 1))
        calc = abs(f - s)
        return calc

    f = min(range(n), key=mad)

    return f
