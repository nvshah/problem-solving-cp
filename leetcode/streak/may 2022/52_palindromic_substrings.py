# https://leetcode.com/problems/palindromic-substrings/

from itertools import starmap 
from operator import eq

def isPalindrome(s):
    m = len(s) // 2
    return all(starmap(eq, zip(s[:m], reversed(s))))

def countSubstrings(s: str) -> int:
    length = len(s)
    res = 0
    for l in range(length):
        for r in range(l, length):
            res += isPalindrome(s[l:r+1])
    
    return res