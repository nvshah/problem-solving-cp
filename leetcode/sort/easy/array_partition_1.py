# https://leetcode.com/problems/array-partition-i/discuss/1624649/python-solution-using-sort-suitable-comments

from typing import List


def arrayPairSum(nums: List[int]) -> int:
    nums.sort()
    return sum(nums[::2])
