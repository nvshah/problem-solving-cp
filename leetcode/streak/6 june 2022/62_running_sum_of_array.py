# https://leetcode.com/problems/running-sum-of-1d-array/

from typing import List


def runningSum(nums: List[int]) -> List[int]:
    return it.accumulate(nums)