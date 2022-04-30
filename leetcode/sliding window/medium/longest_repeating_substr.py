# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

from collections import defaultdict

def longestSubstring(s: str, k: int) -> int:
    '''
        O(n)
        Idea :- Try to explore window  
                Expand -> until repeating character found
                Shrink -> until non-repeating chara found   
    '''
    res = 0  # max-length of window

    l = 0
    freq = 0
    for r in range(len(s)):
        


    return res