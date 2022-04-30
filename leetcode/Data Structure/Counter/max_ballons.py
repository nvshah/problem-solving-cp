# https://leetcode.com/problems/maximum-number-of-balloons/
from collections import Counter

def maxNumberOfBalloons(text: str) -> int:
    cnts = Counter(text)
    freq = Counter('balloon')
    return min([cnts[c]//freq[c] for c in freq])