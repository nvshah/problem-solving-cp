# https://leetcode.com/problems/find-the-highest-altitude/description/

from itertools import accumulate
from typing import List


def largestAltitude(gain: List[int]) -> int:
    return max(accumulate(gain, initial=0))