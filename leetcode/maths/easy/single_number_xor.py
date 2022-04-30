# https://leetcode.com/problems/single-number/

from typing import List
from functools import reduce
from operator import xor

def singleNumber(nums: List[int]) -> int:
    return reduce(xor, nums)  # all duplicate double number will cancel each other