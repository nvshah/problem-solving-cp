# https://leetcode.com/problems/palindrome-pairs/
from telnetlib import WILL
from typing import List

def isPal(s, l=0, r=None):
    if not s: return True
    r = r or len(s)-1
    
    while l<r:
        if s[l] != s[r]: return False 
        l, r = l+1, r-1 
    return True 

def palindromePairs(words: List[str]) -> List[List[int]]:
    # 1. Create a lookup for word -> pos
    lookup = {w:i for i,w in enumerate(words)}
    ans = []

    # Find palindromes for all words
    status = [1 if isPal(words[i]) else 0 for i in range(len(words))]

    for i, w in enumerate(words):
        if not w: 
            for j in range(len(words)):
                if i == j: continue 
                if status[j]:
                    ans.extend([(i, j), (j, i)])

        size = len(w)
        rev = w[::-1]
        # Check for entire word match
        if rev in lookup and lookup[rev] != i:
            ans.append((i, lookup[rev]))

        for k in range(1, size): # r -> exclusive index
            # [w] as a right side of palindrome | checking possibilities
            if isPal(w, 0, k-1):
                rest = w[k:]
                left = rest[::-1]
                if left in lookup: # found match => left side candidate
                    ans.append((lookup[left], i))

            # [w] as a left side of palindrome | checking possibilities
            if isPal(w, k, size-1):
                pre = w[:k]
                right = pre[::-1]
                if right in lookup:
                    ans.append((i, lookup[right]))

    return ans 


