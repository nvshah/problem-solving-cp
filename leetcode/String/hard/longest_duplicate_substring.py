# https://leetcode.com/problems/longest-duplicate-substring/

from functools import partial


import operator as op

import itertools as it

def longestDupSubstring(s: str) -> str:
    '''
    via suffix Array & Longest Common Prefix Arrays (O(n * log(n)))
    '''
    size = len(s)

    def commonPrefixSize(s1, s2, start=0):  
        ''' Find common prefix lenght from starting index between 2 string'''
        cLen = min(len(s1), len(s2))  # exhausting length
        s = 0
        if start < cLen:
            for c1, c2 in zip(s1[start:], s2[start:]):
                if c1 != c2:
                    return s 
                s += 1
        return s

    # 1. Suffix Array
    sa = sorted(range(size), key=lambda i: s[i:])  

    # 2. Rank Array = Invert of Suffix Array
    ra = [0]*size   
    for r, i in enumerate(sa):
        ra[i] = r 

    # 3. Kasai Algo to Find LCP array  (in O(n)) time
    lcp = [0]*size  # Longest Common Prefix Array

    skip = 0  # number of prefix going to be common for next comparision (so we can skip those characters in next comparision)
    for i in range(size):
        rank = ra[i]
        if rank == 0: continue 

        p = sa[rank-1] # find prev suffix index
        curr = s[i:]
        prev = s[p:]

        common = lcp[rank] = skip + commonPrefixSize(curr, prev, skip)

        #next = max(0, common - 1)
        skip = max(0, common - 1)

    # 4. LDS = max value in longest common prefix
    rank = max(range(size), key=lcp.__getitem__)
    u = lcp[rank]  # upper bound = longest duplicate substring size
    l = sa[rank]   # lower bound = original staring index of suffix
    lds = s[l: l+u]

    return lds


def longestDupSubstring2(self, s: str) -> str:
    ans = ''
    j   = 1
    for i in range(len(s)):
        longest = s[i:i+j]
        temp    = s[i+1:]
        while longest in temp:
            ans = longest
            j += 1
            longest = s[i:i+j]
    return ans

s = "banana"
s = "abcd" 
print(longestDupSubstring(s))