# https://leetcode.com/contest/biweekly-contest-77/problems/count-prefixes-of-a-given-string/
from typing import List

def countPrefixes(words: List[str], s: str) -> int:
    cnt = 0
    l = len(s)
    for w in words:
        if len(w) <= l and s.startswith(w):
            cnt += 1
    return cnt