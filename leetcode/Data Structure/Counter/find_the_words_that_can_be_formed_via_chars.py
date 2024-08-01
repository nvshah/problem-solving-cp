# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
from typing import List
from collections import Counter, defaultdict



def countCharacters(words: List[str], chars: str) -> int:
    '''Counter | DefaultDict'''
    domain = Counter(chars)
    res = 0

    for word in words:
        charMap = defaultdict(int)
        for c in word:
            if charMap[c] == domain[c]: # not possible
                break
            charMap[c] += 1
        else:
            res += len(word)
    
    return res 


def countCharacters(words: List[str], chars: str) -> int:
    charsCount = Counter(chars)
    res = 0

    for word in words:
        freqs = Counter(word)
        fulfilled = all(freqs[c] <= charsCount[c] for c in freqs)
        if fulfilled:
            res += len(word)
    
    return res 