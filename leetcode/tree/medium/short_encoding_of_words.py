# https://leetcode.com/problems/short-encoding-of-words/
from collections import defaultdict
from typing import List

class TrieNode:
    # instance of {TrieNode} represent a letter
    def __init__(self):
        # children := letter -> Node mapping at curr level
        self.children = defaultdict(TrieNode)  # holds info abt possible following letters
        # is this (ie Node's) letter is end of any word registered
        self.isEndOfWord = False  # is this TrieNode

class Trie:

    def __init__(self):
        self.root = TrieNode()  # placeholder root node
        self.depths = []
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children[c]  # find Node corresp to letter {c} & advance it
        
        if len(cur.d) == 0:
            self.depths.append(len(word) + 1) # +1 for `#`

def minimumLengthEncoding(words: List[str]) -> int:
    t = Trie()
    s = set(words)
    for w in s:  # as we want to check Suffix
        t.insert(w[::-1])
    
    return sum(t.depths)
