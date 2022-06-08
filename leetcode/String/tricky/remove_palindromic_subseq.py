# https://leetcode.com/problems/remove-palindromic-subsequences/submissions/

from itertools import starmap
from operator import eq


def isPalindrome(s):
    m = len(s) // 2
    return all(starmap(eq, zip(s[:m], reversed(s))))

'''Approach 1'''
def removePalindromeSub1(s: str) -> int:
    return 1 if isPalindrome(s) else 2 


def removePalindromeSub2(s: str) -> int:
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]: return 2
        l, r = l+1, r-1
    
    return 1

    