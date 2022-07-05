# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

from itertools import pairwise, starmap
from operator import sub
from typing import List


def maxArea(h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
    # Sorted inorder to get max gap horizontally & vertically
    hPos = [h, *sorted(horizontalCuts, reverse=True), 0]
    vPos = [w, *sorted(verticalCuts, reverse=True), 0]
    
    maxHeight = max(starmap(sub, pairwise(hPos)))
    maxWidth = max(starmap(sub, pairwise(vPos)))
    
    return (maxHeight * maxWidth) % (10**9 + 7)