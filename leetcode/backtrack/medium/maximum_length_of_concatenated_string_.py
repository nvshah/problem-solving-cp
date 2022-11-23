# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
from typing  import List
from collections import Counter

class Solution2:
    # BACKTRACKING
    def maxLength(self, arr: List[str]) -> int:
        size = len(arr)
        charSet = set()  # current set of characters part of concatenated string

        def overlap(s1, s2):
            return len(s1.union(s2)) != len(s1) + len(s2)
        
        def backtrack(i):   
            ''' Return the lenngth of concatenated string'''
            if i == size: return len(charSet)  # no more char can be added !

            length = 0  # cur count of chars in {charSet}
            if not overlap(charSet, arr[i]):     # Accounting curr word ie arr[i]
                charSet.update(arr[i])     # Pick
                length = backtrack(i+1)    # Explore
                charSet.difference_update(arr[i])  # UnPick (Backtrack)

            return max(length, backtrack(i+1)) # Without current Word ie arr[i]
        
        return backtrack(0)

class Solution1:
    # RECURSIVE (TOP-DOWN)
    def maxLength(self, arr: List[str]) -> int:
        size = len(arr)

        def hasUniqueChars(s1, s2):
            #for c in s:
            union = s1.union(s2)
            return len(union) == len(s1) + len(s2)
        
        def helper(i, charset):   
            ''' Return the lenngth of concatenated string'''
            if i == size:
                return len(charset)

            length = 0  # cnt of characters via this way (return from backtrack)

            # Pick {i}
            if hasUniqueChars(charset, arr[i]):
                length = helper(i+1, charset.union(arr[i]))

            # UnPick {i} 
            return max(length, helper(i+1, charset))
        
        return helper(0, set())
