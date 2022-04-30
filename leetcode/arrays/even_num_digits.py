# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

from typing import List
from math import log10
from functools import reduce


def isEvenDigits(n):
    digits = int(log10(abs(n))) + 1
    return 1-(digits & 1)


def findNumbers(nums: List[int]) -> int:
    return reduce(lambda x, y: x + isEvenDigits(y), nums, 0)


def findNumbers2(nums: List[int]) -> int:
    return len([None for n in nums if isEvenDigits(n)])


nums = [12, 345, 2, 6, 7896]

print(findNumbers(nums))
