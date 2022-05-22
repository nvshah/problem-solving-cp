# https://leetcode.com/problems/palindromic-substrings/

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