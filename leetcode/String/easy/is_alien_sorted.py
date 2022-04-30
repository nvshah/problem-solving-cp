# https://leetcode.com/problems/verifying-an-alien-dictionary/

from typing import List
import itertools as it

def isAlienSorted(words: List[str], order: str) -> bool:
    lex = {c:i for i,c in enumerate(order)}
    # for i in range(len(words)-1):
    #         w1, w2 = words[i], words[i+1]
    for w1, w2 in it.pairwise(words):
        w1Len, w2Len = len(w1), len(w2)
        minLen = min(w1Len, w2Len)

        for i in range(minLen):
            s1, s2 = lex[w1[i]], lex[w2[i]]  # score 1, score 2
            if s1 > s2:  # incorrect lexiographic
                return False
            if s1 < s2:
                break
        else:
            # all characters are same (till minLen)
            if w1Len > w2Len: # if w1 is larger than w2 then its incorrect lexiographically
                return False
    return True

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

print(isAlienSorted(words, order))