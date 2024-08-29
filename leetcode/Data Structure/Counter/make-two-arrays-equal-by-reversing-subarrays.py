# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

from typing import List
from collections import Counter, defaultdict

'''
As infinite reverse attempts are allowed for sub-arrays
We can place each and individual element to its correct loc, one by one
Now
Only thing is that we must have same numbers of candidate available in [arr] as of [target]
i.e
[target] & [arr] if are **anagram** of each other its possible to restore [arr] to [target] with reversing sub-arr operations. 

'''

def isAnagram(a1, a2):
    return Counter(a1) == Counter(a2) 

def isAnagram_A2(a1, a2):
    count1, count2 = defaultdict(int), defaultdict(int)
    for n1, n2 in zip(a1, a2):
        count1[n1] += 1
        count2[n2] += 1 

    return count1 == count2  


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return isAnagram(target, arr)
        

