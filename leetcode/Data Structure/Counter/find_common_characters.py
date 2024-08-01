# https://leetcode.com/problems/find-common-characters/description/
from collections import Counter
from typing import List 
from operator import and_
from functools import reduce

# MultiSets

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freqs = reduce(and_, map(Counter, words))
        return min_freqs.elements() # multiset representation

class Solution2:
    def commonChars(self, words: List[str]) -> List[str]:
        freqs = Counter(words[0])

        for word in words[1:]:
            cur_freqs = Counter(word) 
            for c in freqs:
                freqs[c] = min(freqs[c], cur_freqs[c])

        return freqs.elements()
    
class Solution3:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freqs = Counter(words[0])

        for word in words[1:]:
            min_freqs &= Counter(word) 

        return min_freqs.elements()