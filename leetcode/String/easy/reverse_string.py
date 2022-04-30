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


def reverseString2(s: List[str]) -> None:
    """
    In-Place
    via Stack Aid | Iterative Algo
    (Time Efficient)
    """
    # 1. Pour
    stack = [c for c in s] 
    # 2. Remove
    for i in range(len(s)):
        s[i] = stack.pop()

def reverseString3(s: List[str]) -> None:
    """
    In-Place 
    via 2 pointers | Recursive Algo
    Its not a Constant time Complexity as Recursive takes memory on call-stack
    (Less Efficient)
    """
    def rev(l, r):
        if l < r:
            s[l], s[r] = s[r], s[l]
            rev(l+1, r-1)  # this is less efficient as we are using Space from Recursive Call Stack
    
    rev(0, len(s)-1)
