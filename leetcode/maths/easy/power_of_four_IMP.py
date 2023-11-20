# https://leetcode.com/problems/power-of-four/

from math import log


def isPowerOfFour(n: int) -> bool:
    if n == 1: return True
    if n < 4: return False
    e = log(n) / log(4)
    return e//1 == e