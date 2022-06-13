# https://leetcode.com/problems/remove-palindromic-subsequences/
from itertools import starmap 
from operator import eq

def isPalindrome(s):
    m = len(s) // 2
    return all(starmap(eq, zip(s[:m], reversed(s))))

def removePalindromeSub(s: str) -> int:
    return 1 if isPalindrome(s) else 2 