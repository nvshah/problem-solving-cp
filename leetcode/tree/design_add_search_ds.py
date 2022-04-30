# https://leetcode.com/problems/design-add-and-search-words-data-structure/
from collections import defaultdict

class TrieNode:
    ''' TrieNode represents a single letter in a Tree Structure (TRIE) '''
    def __init__(self):
        # children := nodes of possible following characters to this {self} letter
        #             // this children nodes will lie on 1 layer below the current layer
        self.children = defaultdict(TrieNode)
        self.isEndOfWord = False  # does this letter is suggesting end of any word

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()  # placeholder node

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        '''Recursive + Iterative'''
        l = len(word)
        def dfs(s, node):
            ''' from i idx till end of word, find the word in Tree by starting search from {node} '''
            cur = node
            for i in range(s, l):
                c = word[i]
                if c == '.':
                    for n in cur.children.values():  # visit all nodes at below level
                        if dfs(i+1, n):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]        # go to next layer
            return cur.isEndOfWord
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)