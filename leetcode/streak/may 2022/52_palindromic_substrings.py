# https://leetcode.com/problems/palindromic-substrings/

from itertools import starmap 
from operator import eq

'''Via 2 Ends Appraoch'''
def isPalindrome(s):
    m = len(s) // 2
    return all(starmap(eq, zip(s[:m], reversed(s))))

'''Brute Force O(n^3)'''
def countSubstrings1(s: str) -> int:
    length = len(s)
    res = 0
    for l in range(length):
        for r in range(l, length):
            res += isPalindrome(s[l:r+1])
    
    return res

'''Via Centric approach'''


'''Brute Force O(n^2) <-- Better '''
def countSubstrings2(s: str) -> int:
    res = 0
    sz = len(s)

    def cntPalindrome(l, r):
        while l >= 0 and r < sz:
            if s[l] != s[r]:
                break 
            res += 1
            l, r = l-1, r+1

    for i in range(len(s)):
        print(res)
        # consider {i} pos as center for palidrome substring & find all possible substring
        # 1. Odd length Palindrome
        l = r = i 
        cntPalindrome(l, r)
        # 2. Even Length Palindrome
        l, r = i, i+1
        cntPalindrome(l, r)

    return res 

s = "aaa"
a = countSubstrings2(s)
print(a)
