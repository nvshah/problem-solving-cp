# https://leetcode.com/problems/binary-trees-with-factors/

from collections import defaultdict
from typing import List


def numFactoredBinaryTrees(arr: List[int]) -> int:
    arr.sort()
    lookup = defaultdict(int)
    s = set(arr)
    
    for i, a in enumerate(arr):
        ways = 1 # itself as root for [a]
        # check for children possibility
        for j in range(i):
            f1 = arr[j]
            f2, r = divmod(a, f1)
            if r == 0 and f2 in s:
                ways += lookup[f1] * lookup[f2]
        lookup[a] = ways
    
    return sum(lookup.values()) % (10**9 + 7)