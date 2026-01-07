# https://leetcode.com/problems/xor-queries-of-a-subarray

from typing import List
from itertools import accumulate
from operator import xor


def xorQueries(arr: List[int], queries: List[List[int]]) -> List[int]:
    # for given position i ->
    # - It will hold xors till i (excluding i) (ie xors of arr[0:i])
    prefix_xors = [*accumulate(arr, xor, initial=0)]
    res = []
    for l, r in queries:
        # as l & r are inclusive of the query-sublist
        before_l = prefix_xors[l]  # prefix xor
        upto_r = prefix_xors[r + 1]  # prefix xor
        res.append(before_l ^ upto_r)
    return res
