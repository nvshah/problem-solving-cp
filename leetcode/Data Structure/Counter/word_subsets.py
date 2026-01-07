# https://leetcode.com/problems/word-subsets/
from collections import Counter, defaultdict
from typing import List
from operator import methodcaller, itemgetter
from itertools import chain

def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    # all letters of words2 with highest frequency
    target = defaultdict(int)
    for word in words2:
        freq = Counter(word)
        for letter, count in freq.items():
            target[letter] = max(target[letter], count)

    res = []
    for word in words1:
        freq = Counter(word)
        if all(freq[letter] >= target[letter] for letter in target):
            res.append(word)

    return res
