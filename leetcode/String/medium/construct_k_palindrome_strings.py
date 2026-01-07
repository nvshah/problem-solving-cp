# https://leetcode.com/problems/construct-k-palindrome-strings/
from collections import Counter

'''
 # at-most k single freq letter
 # ie if there are lesser or no odd count letters then we can easily account the palindrome by settling even counts
'''

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        freq = Counter(s)
        odds_count = sum(n & 1 for n in freq.values())
        # constructing k diff palindrome requires
        # at most k single letters
        return odds_count <= k
