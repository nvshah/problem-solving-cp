# https://leetcode.com/problems/number-of-matching-subsequences/

from bisect import bisect
from collections import defaultdict
from typing import List

def numMatchingSubseq(s: str, words: List[str]) -> int:
    lookup = defaultdict(list)
    for i, c in enumerate(s):
        lookup[c].append(i)
    cnt = 0
    for w in words:
        prev = -1
        for c in w:
            lst = lookup[c]
            # get the right next index to [prev] from [lst]
            i = bisect(lst, prev)
            if i == len(lst):   # no index is found closest to [prev] on right side in [lst]
                break
            prev = lst[i]
        else:
            cnt += 1
    return cnt

s = "dsahjpjauf"
w = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]

s="abcde"
w=["a","bb","acd","ace"]

ans = numMatchingSubseq(s, w)
print(ans)
