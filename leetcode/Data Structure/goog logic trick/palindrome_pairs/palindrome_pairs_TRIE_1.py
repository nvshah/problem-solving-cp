from collections import defaultdict
from itertools import starmap
from operator import eq
from typing import List

''' VIA TRIE (But this is Taking much time)'''


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
        self.children = [None]*26  # holds info abt possible following letters
        # is End of word & [index] holds the position of words in original List
        self.index = -1
        # Holds the indexes of words from original list -> whose sub-str is palindrome till this node (ie character)
        # this will be useful if [index] >=0 (ie node is last character of any word)
        self.lst = [] # indexes of word that contain curr-sub word as palindrome

class Trie:

    def __init__(self):
        self.root = TrieNode()  # placeholder root node
        
    def insert(self, word: str, pos: int) -> None:
        cur = self.root
        for i in range(len(word)-1, -1, -1):
            char = word[i]
            offset = ord(char) - ord('a')

            if not cur.children[offset]:
                cur.children[offset] = TrieNode()

            # Check if the sub-word (ie word[:i+1]) is palindrome or not
            if isPalindrome(word[:i+1]):
                cur.lst.append(pos)
            
            # Get to the next level
            cur = cur.children[offset]  # find Node corresp to letter {c} & advance it
        
        # For empty String at start (its always palindrome)
        cur.lst.append(pos)

        # NOTE -> constraint is give that all words are unique so this index -> 1 pos
        cur.index = pos # mark end of word & position track

    def search(self, word: str, pos: int, res) -> bool:
        cur = self.root
        for i, c in enumerate(word):
            offset = ord(c) - ord('a')
            # Checking this condition first because trailing empty string lies at the root
            # Look for Trailing Sub-Str of [word]
            if cur.index != -1 and cur.index != pos and isPalindrome(word[i:]):
                res.append((pos, cur.index))

            cur = cur.children[offset]
            if not cur: return 

        # Look for Leading sub-str of partner word
        # Check other words that can contain this [word] as a substring & rest is palindrome
        for idx in cur.lst:
            if idx == pos: continue
            res.append((pos, idx))

        return res

    
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        t = Trie()
        ans = []

        for i, w in enumerate(words):
            t.insert(w, i) 

        for i, w in enumerate(words):
            t.search(w, i, ans)

        return ans
