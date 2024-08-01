# https://leetcode.com/problems/score-of-a-string/?envType=daily-question&envId=2024-06-01

from itertools import pairwise

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        asciis = map(ord, s)
        for cur, nxt in pairwise(asciis):
            score += abs(cur-nxt)
        return score
    
    def scoreOfString2(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i+1]))
        return score