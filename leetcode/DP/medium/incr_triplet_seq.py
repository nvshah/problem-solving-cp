# https://leetcode.com/problems/increasing-triplet-subsequence/

from typing import List


def increasingTriplet(nums: List[int]) -> bool:
    MAX = (2**31)-1
    f = s = MAX  # first & second increasing val
    
    for n in nums:
        if n <= f: f = n
        elif n <= s: s = n
        else: return True
    return False