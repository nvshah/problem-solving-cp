# Que -> https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

from typing import List
from math import log10
from functools import reduce


def isEvenDigits(n):
    digits = int(log10(abs(n))) + 1
    return not(digits & 1)


def findNumbers(nums: List[int]) -> int:
    c = 0
    for num in nums:
        if isEvenDigits(num):
            c += 1
    return c


def findNumbers2(nums: List[int]) -> int:
    return reduce(lambda x, y: (isEvenDigits(y) + x), nums, 0)


def findNumbers3(nums: List[int]) -> int:
    return len([None for n in nums if isEvenDigits(n)])


nums = [12, 345, 2, 6, 7896]
ans = findNumbers2(nums)

print(ans)
