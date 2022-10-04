from itertools import chain
from typing import List

# QUE https://leetcode.com/problems/palindrome-pairs

'''WORKING & EFFICIENT SOln'''

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # list of (index, word, is_reversed), `word` can be either a orginal word or a reversed word
        # the list is sorted so that words with similar prefix are consecutive
        words = sorted(chain(((i, w, False) for i, w in enumerate(words)), 
                             ((i, w[::-1], True) for i, w in enumerate(words))),
                             key=lambda x: x[1])
        
        # Loop through each word         
        for i, (idx1, w1, is_reversed1) in enumerate(words):
            # Look at each word (w2) after the current word (w1) to find a prefix of the current word
            # When w1 is a prefix of w2 then w1 + w2[::-1] is a palindrome
            # Because the words are sorted, if w1 is a prefix of w2 then w1 will come before w2, so we only need to start from i + 1
            for j in range(i + 1, len(words)):
                idx2, w2, is_reversed2 = words[j]
                if w2.startswith(w1):
                    # we want one of w1 and w2 is a reversed word
                    # because if w1 is a prefix of w2 but both w1 and w2 are in the orginal words then w1 + w2[::-1] cannot be a palindrome
                    if is_reversed1 == is_reversed2:
                        continue
                    rest = w2[len(w1):]
                    # check idx1 != idx2 for cases where a word is a palindrome its self
                    # then check whether the postfix of w2 is a palindrome
                    if idx1 != idx2 and rest == rest[::-1]:
                        # if w1 is an original word and w2 is a reversed word, then w1 + w2[::-1] is a palindrome => return (idx1, idx2)
                        # otherwise w1 + w2[::-1] = w2 + w1[::] is a palindrome => return (idx2, idx1)
                        yield (idx1, idx2) if is_reversed2 else (idx2, idx1)
                else:
                    # because the words are sorted, so if we found a word that is not a prefix of the curent word 
                    # then every word after that can't be a prefix of the current word
                    break
