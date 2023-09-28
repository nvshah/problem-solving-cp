

from collections import defaultdict
from typing import List

''' With this method 1 Test Case is Failing for 
   `Time Limit Exceeding Error`
'''

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
        self.cache = {}  # word -> is available/composable or not
        self.wordSet = set()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children[c]  # find Node corresp to letter {c} & advance it
        cur.isEndOfWord = True  # as last letter marks end of word
        self.wordSet.add(word)

    def isAvailable(self, word):
        '''DFS'''
        if not word: return True

        if word in self.wordSet:
            self.cache[word] = True 
            return True
        if word in self.cache:
            return self.cache[word]
        
        cur = self.root 
        for i, c in enumerate(word):
            if c not in cur.children:
                return False 
            cur = cur.children[c]
            if cur.isEndOfWord and self.isAvailable(word[i+1:]):
                self.cache[word] = True
                return True 
        self.cache[word] = False
        return False

    
    def canBreak(self, word: str) -> bool:
        cur = self.root
        for i, c in enumerate(word):
            cur = cur.children[c] 
            if cur.isEndOfWord:
                suffix = word[i+1:]
                if suffix:
                    if self.isAvailable(suffix):
                        return True 
        return False

                # check for rest

def findAllConcatenatedWordsInADict(words: List[str]) -> List[str]:
    trie = Trie()
    for w in words: 
        trie.insert(w)
    
    res = [w for w in words if(trie.canBreak(w))]
    print(res)


words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
words = ["cat","dog","catdog"]
ans = findAllConcatenatedWordsInADict(words)
print(ans)