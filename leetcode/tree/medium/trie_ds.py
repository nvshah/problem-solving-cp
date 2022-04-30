# https://leetcode.com/problems/implement-trie-prefix-tree/submissions/
from collections import defaultdict

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
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children[c]  # find Node corresp to letter {c} & advance it
        cur.isEndOfWord = True  # as last letter marks end of word

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children: # if letter {c} is not found in corresp layer
                return False
            cur = cur.children[c]
        # check if last letter is marked end of word
        return cur.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children: # if letter {c} is not found in corresp layer
                return False
            cur = cur.children[c]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)