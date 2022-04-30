# https://leetcode.com/problems/find-the-highest-altitude/

from typing import List
import itertools as it


def largestAltitude(gain: List[int]) -> int:
    return max(it.accumulate(gain, initial=0))


def largestAltitude2(gain: List[int]) -> int:
    m = l = 0
    for g in gain:
        l = l + g
        m = max(m, l)
    return m


gain = [-5, 1, 5, 0, -7]
#gain = [-4, -3, -2, -1, 4, 3, 2]
ans = largestAltitude2(gain)

print(ans)
