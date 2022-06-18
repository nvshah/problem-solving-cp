# https://leetcode.com/problems/prefix-and-suffix-search/
from collections import defaultdict
from typing import List

'''
Idea :- Trie + Caching
'''

class TrieNode:
    # instance of {TrieNode} represent a letter
    def __init__(self):
        # children := letter -> Node mapping at curr level
        self.children = defaultdict(TrieNode)  # holds info abt possible following letters
        self.ids = set()  # ids corresp to words that share current trie-node

class Trie:

    def __init__(self):
        self.rootP = TrieNode()  # placeholder root node for Prefix Tree
        self.rootS = TrieNode() # placeholder for Suffix Tree 
        
    def insertInPrefixTree(self, word: str, id: int) -> None:
        cur = self.rootP
        for c in word:
            cur = cur.children[c]  # find Node corresp to letter {c} & advance it
            cur.ids.add(id)
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.rootP
        for c in prefix:
            if c not in cur.children: # if letter {c} is not found in corresp layer
                return False
            cur = cur.children[c]
        return cur.ids 

    def insertInSuffixTree(self, word: str, id: int) -> None:
        cur = self.rootS
        for c in reversed(word):
            cur = cur.children[c]  # find Node corresp to letter {c} & advance it
            cur.ids.add(id)

    def endsWith(self, suffix: str) -> bool:
        cur = self.rootS
        for c in reversed(suffix):
            if c not in cur.children: # if letter {c} is not found in corresp layer
                return False
            cur = cur.children[c]
        return cur.ids

class WordFilter:

    def __init__(self, words: List[str]):
        t = Trie()
        
        for i, w in enumerate(words):
            t.insertInPrefixTree(w, i)
            t.insertInSuffixTree(w, i)
        
        self.words = words
        self.trie = t
        self.cache = {}
        
    def f(self, prefix: str, suffix: str) -> int:
        k = (prefix, suffix)
        if k in self.cache:
            return self.cache[k]
        
        pIdx = self.trie.startsWith(prefix)
        if not pIdx:
            self.cache[k] = -1 
            return -1
        sIdx = self.trie.endsWith(suffix)
        if not sIdx: 
            self.cache[k] = -1 
            return -1

        common = pIdx & sIdx

        v = max(common) if common else -1
        self.cache[k] = v
        return v


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


#w = WordFilter(["apple", "arcone", "arilssde"])
#idx = w.f('ar', 'e')

#["WordFilter","f","f","f","f","f","f","f","f","f","f"]
#[[["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]],
#["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]]

# lst = ["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa","accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]
# w = WordFilter(lst)
# idx = w.f("a", "aa")

lst = ["abbba", "abba"]
w = WordFilter(lst)
idx = w.f("ab", "ba")

print(idx)