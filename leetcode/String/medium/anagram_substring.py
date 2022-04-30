# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from typing import List
from collections import defaultdict as dd
from collections import Counter as ctr


def findAnagrams1(s: str, p: str) -> List[int]:
    len_s = len(s)
    len_p = len(p)

    if len_p > len_s:
        return []

    ans = []
    
    p_count = {}  # keep count of all characters in string {p}
    s_count = {}  # keep count of characters in current window 

    for i in range(len_p):
        p_count[p[i]] = 1 + p_count.get(p[i], 0)
        s_count[s[i]] = 1 + s_count.get(s[i], 0)

    if s_count == p_count: # match at starting of string {s}
        ans.append(0)

    l = 0  # left pointer of Sliding Window

    # throught rest part of string s after p-character
    for r in range(len_p, len_s):
        l_chr, r_chr = s[l], s[r] 
        s_count[r_chr] = 1 + s_count.get(r_chr, 0)
        s_count[l_chr] -= 1

        if s_count[l_chr] == 0:
            del s_count[l_chr]  # remove the l_chr ie out of window from dictionary

        l += 1 # update left bound of slidign window
        
        # compare 2 altering characters
        if s_count == p_count:
            ans.append(l)
        
    return ans 

def findAnagrams2(s: str, p: str) -> List[int]:
    len_s = len(s)
    len_p = len(p)

    if len_p > len_s:
        return []
    
    if len_p == len_s:
        return [0] if ctr(p) == ctr(s) else []

    ans = []
    
    p_count = dd(int)  # keep count of all characters in string {p}
    s_count = dd(int)  # keep count of characters in current window

    prev_window_status = False  # if prev_window was anagram of p 

    for i in range(len_p):
        p_count[p[i]] += 1
        s_count[s[i]] += 1

    if s_count == p_count: # match at starting of string {s}
        ans.append(0)
        prev_window_status = True

    l = 0  # left pointer of Sliding Window

    # throught rest part of string s after p-character
    for c in s[len_p:]:
        l_chr = s[l] 
        s_count[c] += 1
        s_count[l_chr] -= 1

        if s_count[l_chr] == 0:
            del s_count[l_chr]  # remove the l_chr ie out of window from dictionary

        l += 1 # update left bound of slidign window
        
        # compare 2 altering characters
        if prev_window_status:
            if c == l_chr:
                ans.append(l)
                prev_window_status = True
            else:
                prev_window_status = False
        elif s_count == p_count:
            ans.append(l)
            prev_window_status = True 
        else:
            prev_window_status = False
        
    return ans 

s = "cbaebabacd"
p = "abc"

s = "abab"
p = "ab"

ans = findAnagrams1(s, p)

print(ans)

        
        
