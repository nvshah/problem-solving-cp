from collections import defaultdict
from itertools import starmap
from operator import eq
from typing import List

'''VIA TRIE (Mine Custom Approach)'''


def isPalindrome(s, l=0, r=None):
    # if not s: return True
    # return all(starmap(eq, zip(s, reversed(s))))
    r = r or len(s)-1
    while l < r:
        if s[l] != s[r]: return False 
        l, r = l+1, r-1
    return True 

class TrieNode:
    # instance of {TrieNode} represent a letter
    def __init__(self):
        # children := letter -> Node mapping at curr level
        self.children = defaultdict(TrieNode)  # holds info abt possible following letters
        # is End of word & [index] holds the position of words in original List
        self.index = -1
        # Holds the indexes of words from original list -> whose sub-str is palindrome till this node (ie character)
        # this will be useful if [index] >=0 (ie node is last character of any word)
        self.idxs = set() # indexes of word that contain curr-sub word as palindrome

class Trie:

    def __init__(self):
        self.root = TrieNode()  # placeholder root node
        
    def insert(self, word: str, pos: int) -> None:
        cur = self.root
        for i in range(len(word)-1, -1, -1):
            # Check if the sub-word (ie word[:i+1]) is palindrome or not
            if isPalindrome(word[:i+1]):
                cur.idxs.add(pos)
            
            # Get to the next level
            cur = cur.children[word[i]]  # find Node corresp to letter {c} & advance it
        
        # NOTE -> constraint is give that all words are unique so this index -> 1 pos
        cur.index = pos # mark end of word & position track

    def search(self, word: str, pos: int) -> bool:
        cur = self.root
        ans = []
        for i, c in enumerate(word):
            if c not in cur.children: # if letter {c} is not found in corresp layer
                return ans 

            cur = cur.children[c]
            
            # Look for Trailing Sub-Str of [word]
            if cur.index != -1 and cur.index != pos and isPalindrome(word[i+1:]):
                ans.append((pos, cur.index))

        # Look for Leading sub-str of partner word
        # Check other words that can contain this [word] as a substring & rest is palindrome
        for idx in cur.idxs:
            ans.append((pos, idx))

        return ans

    def getAllPalindromesPositions(self):
        return self.root.idxs
        

    
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        t = Trie()
        ans = []

        for i, w in enumerate(words):
            t.insert(w, i) 

        # total palindromes
        palPos = t.getAllPalindromesPositions()

        for i, w in enumerate(words):
            if not w:
                for p in palPos: 
                    ans.extend([(p, i), (i, p)])
            else:
                r = t.search(w, i)
                ans.extend(r)

        return ans
