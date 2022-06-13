# https://leetcode.com/problems/is-subsequence/

def isSubsequence(s: str, t: str) -> bool:
    ''' 2 Pointers way'''
    i = j = 0
        
    l1, l2 = len(s), len(t)
    while i < l1 and j < l2:
        if s[i] == t[j]:
            i += 1
        j += 1
    
    return i == l1
