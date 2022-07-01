# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

'''
Que
A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.
'''

from collections import Counter


def minDeletions(s: str) -> int:
    cnts = sorted(Counter(s).values(), reverse=True)
    
    allowed = cnts[0]-1
    res = 0
    
    if not allowed:
        return sum(cnts[1:], 0)
    
    for i in range(1, len(cnts)):
        cnt = cnts[i]
        if cnt > allowed:
            res += cnt-allowed
        allowed = min(allowed-1, cnt-1)
        if allowed==0:
            break
    else:
        return res
    
    res += sum(cnts[i+1:], 0)

    return res 

def minDeletions2(s: str) -> int:
    #         Approach 2
    cnts = sorted(Counter(s).values(), reverse=True)
    
    allowed = cnts[0]-1
    res = 0
    
    for cnt in cnts[1:]:
        if cnt > allowed:
            res += cnt-allowed
        allowed = max(0, min(allowed-1, cnt-1))
    
    return res
