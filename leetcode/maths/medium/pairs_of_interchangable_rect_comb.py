# https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/

from typing import List 
from collections import Counter
import operator as op
from itertools import starmap
from math import comb

def interchangeableRectangles(rectangles: List[List[int]]) -> int:
    ratios_freq = Counter(starmap(op.truediv, rectangles))
    return sum([comb(v, 2) for v in ratios_freq.values()])  # comb(n, 2) = n * (n-1) / 2

rectangles = [[4,8],[3,6],[10,20],[15,30]]
print(interchangeableRectangles(rectangles))