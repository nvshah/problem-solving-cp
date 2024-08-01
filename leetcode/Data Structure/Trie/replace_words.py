# https://leetcode.com/problems/replace-words/
from collections import defaultdict
from typing import List

class TrieNode:
    # instance of {TrieNode} represent a letter
    def __init__(self):
        # children := letter -> Node, mapping at curr level
        self.children = defaultdict(TrieNode)  # holds info abt possible following letters
        # is this (ie Node's) letter is end of any word registered
        self.isEnd = False  # is this TrieNode

class Trie:

    def __init__(self):
        self.root = TrieNode()  # placeholder root node
    
    def insert(self, word: str) -> None:
        '''registered [word] as a token in TRIE Data Structure'''
        cur = self.root
        for c in word:
            cur = cur.children[c]  # find Node corresp to letter {c} & advance it
        cur.isEnd = True  # as last letter marks end of word
    
    def getRootOf(self, word: str) -> bool: 
        '''return smallest registered token s.t. [word] start's with token'''
        cur = self.root
        for i, c in enumerate(word):
            if c not in cur.children:
                return None 
            cur = cur.children[c]
            if cur.isEnd:
                return word[:i+1]
        return None

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        # build trie |-> register all root words from dictionary
        for word in dictionary:  
            trie.insert(word)
        
        derivatives = sentence.split(' ')
        roots = []
        for word in derivatives:
            root = trie.getRootOf(word)
            if not root:
                root = word 
            roots.append(root)
        
        return ' '.join(roots)