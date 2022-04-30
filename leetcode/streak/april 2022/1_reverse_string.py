# https://leetcode.com/problems/reverse-string/
from typing import List

def reverseString1(s: List[str]) -> None:
    """
    In-Place 
    via 2 Pointers
    (Memory Efficient)
    """
    l, r = 0, len(s)-1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l, r = l+1, r-1