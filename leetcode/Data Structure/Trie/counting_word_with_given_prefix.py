# https://leetcode.com/problems/counting-words-with-a-given-prefix/description/

from collections import defaultdict
from typing import List


# region helper

class PrefixNode:
    def __init__(self):
        self.children = defaultdict(PrefixNode)
        self.count = 0  # occurrences of this node


class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def register(self, word):
        trav = self.root
        for char in word:
            node = trav.children[char]
            node.count += 1 # attain
            trav = node # step ahead

    def count(self, prefix):
        trav = self.root
        for char in prefix:
            if char not in trav.children:
                return 0
            trav = trav.children[char]
        return trav.count

# endregions


def prefix_count(words: List[str], pref: str) -> int:
    trie = PrefixTree()
    for word in words:
        trie.register(word)
    return trie.count(pref)

words = ["pay","attention","practice","attend"]
words = ["leetcode","win","loops","success"]
ans = prefix_count(words, "at")
print(ans)