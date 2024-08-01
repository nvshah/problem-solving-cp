# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/


from itertools import chain, starmap, zip_longest
from operator import eq
from typing import List


def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    pairs = zip_longest(chain.from_iterable(word1), chain.from_iterable(word2))
    return all(starmap(eq, pairs))

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    '''4 pointers'''
    N1, N2 = len(word1), len(word2)
    i, j = 0, 0 # word1 pointer, word2 pointer
    m, n = 0, 0 # char1 pointer, char2 pointer

    while i < N1 and j < N2:        
        w1, w2 = word1[i], word2[j]

        if w1[m] != w2[n]: return False 

        m, n = m+1, n+1
        if m == len(w1):
            m, i = 0, i+1
        if n == len(w2):
            n, j = 0, j+1

    return i == N1 and j == N2 

def arrayStringsAreEqual2(word1: List[str], word2: List[str]) -> bool:
    return ''.join(word1) == ''.join(word2)