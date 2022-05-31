#https://leetcode.com/problems/maximum-product-of-word-lengths/
from functools import reduce
from itertools import combinations, starmap
from typing import List
from operator import or_

'''
Concept used : 
 -> combinations, starmap, filter, reduce, map, ord, bit
'''



def encode(c):
    return 1 << ord(c)-97

def get_bit_repr(w):
     # let a bitwise repr for 26 letters (ie 26 length encoding)
    vec = map(encode, w)
    bit_w = reduce(or_, vec, 0)
    return bit_w


def prodWordLen(w1, w2):
    return len(w1) * len(w2)

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        #words.sort(key=len, reverse=True)
        
        lookup = {w: get_bit_repr(w) for w in words}
        
        def doNotShareCommonLetters(w1w2):
            w1, w2 = w1w2
            bit_w1 = lookup[w1]
            bit_w2 = lookup[w2]

            return not (bit_w1 & bit_w2)
        
        
        elig = [*starmap(
                    prodWordLen, 
                    filter(doNotShareCommonLetters, combinations(words, 2))),
                0
               ]
        
        # elig = [len(e1) * len(e2) for e1, e2 in combinations(words, 2) if not(set(e1) & set(e2))]
        #elig.append(0)
        return max(elig)