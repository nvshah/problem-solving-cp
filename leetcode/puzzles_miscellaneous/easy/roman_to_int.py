# https://leetcode.com/problems/roman-to-integer/

from itertools import pairwise

def romanToInt(s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    for c1, c2 in pairwise(s):
        v1, v2 = roman[c1], roman[c2]
        if v1 < v2:   # next is less 
            res -= v1
        else:
            res += v1  # next is greater
    res += roman[s[-1]]  # add last character mapping
    return res