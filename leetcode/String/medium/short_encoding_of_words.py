# https://leetcode.com/problems/short-encoding-of-words/
from collections import defaultdict
from typing import List

def minimumLengthEncoding(words: List[str]) -> int:
    n = len(words)
    res = set(words) # set
    
    for w in words:
        if w not in res: continue  # already part of another word
        for i in range(1, len(w)):
            sub = w[-i:]  # trailing sub word
            if sub in res:  # found trailing sub string
                res.remove(sub)
    
    if not res: return 0
    
    return sum(map(len, res)) + len(res)


# -----

class TrieNode:
    # instance of {TrieNode} represent a letter
    def __init__(self):
        # children := letter -> Node mapping at curr level
        self.children = defaultdict(TrieNode)  # holds info abt possible following letters
        

class Trie:

    def __init__(self):
        self.rootS = TrieNode() # placeholder for Suffix Tree 
        

    def insertInSuffixTree(self, word: str, id: int) -> None:
        cur = self.rootS
        for c in reversed(word):
            cur = cur.children[c]  # find Node corresp to letter {c} & advance it
        

    def count_leaf_nodes(self, node, cnt):
        if not node:
            return cnt + 1
        for c in node.children:
            cnt += self.count_leaf_nodes(c, cnt)


def minimumLengthEncoding2(words: List[str]) -> int:
    n = len(words)
    res = set(words) # set

    t = Trie()
    
    for w in words:
        t.insertInSuffixTree(w)

    
        
    if not res: return 0
    
    return sum(map(len, res)) + len(res)