# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

from ast import List
from collections import Counter


def maxLength(arr: List[str]) -> int:
    chars = set()  # set of current unique characters
    size = len(arr)

    def hasUniqueChars(s1, s2):
        #for c in s:
        union = s1.union(s2)
        return len(union) == len(s1) + len(s2)

    def overlap(s1, s2):
        c = Counter(s1) + Counter(s2)
        return c.most_common[1][0][1] != 1  # First most commmon is not single element

    def backtrack(i):   
        ''' Return the lenngth of concatenated string'''
        if i == size:
            return len(chars)
        
        cnt = 0  # cnt of characters via this way (return from backtrack)

        # Pick {i}
        if not overlap(chars, arr[i]):
            chars.update(arr[i])  # add all character to character set
            cnt = backtrack(i+1)
        
        # UnPick {i}  -- BackTrack
        chars.difference_update(arr[i])
        return max(cnt, backtrack(i+1))

    def backtrack2(i, charset):   
        ''' Return the lenngth of concatenated string'''
        if i == size:
            return len(charset)
        
        length = 0  # cnt of characters via this way (return from backtrack)

        # Pick {i}
        if not overlap(charset, arr[i]):
            length = backtrack(i+1, charset.union(arr[i]))
        
        # UnPick {i}  -- BackTrack
        return max(length, backtrack(i+1, charset))

    backtrack2(0, set())



