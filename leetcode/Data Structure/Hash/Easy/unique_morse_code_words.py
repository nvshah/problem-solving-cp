# https://leetcode.com/problems/unique-morse-code-words/

import string
from typing import List

def uniqueMorseRepresentations(words: List[str]) -> int:
    ''' Via Dictionary '''
    table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    chrs = string.ascii_lowercase
    mapp = dict(zip(chrs, table))  # dict from keys & values
    
    r = {''.join(map(mapp.get, w)) for w in words}
    return len(r)

def uniqueMorseRepresentations2(words: List[str]) -> int:
    ''' Via Ordinal '''

    table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    i = ord('a') # initial pos
    r = {''.join(map(lambda c: table[ord(c) - i], w)) for w in words}
    return len(r)