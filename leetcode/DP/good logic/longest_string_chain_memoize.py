# https://leetcode.com/problems/longest-string-chain/
from typing import List

def longestStrChain(words: List[str]) -> int:
    s = set(words)
    cache = {}  # memoization

    def lsc(word):
        ''' Return the max length possible for this word as a part of longest str chain'''
        if word not in s: return 0 
        if word in cache: return cache[word]

        l = len(word)
        cnt = 0
        for i in range(l):
            skip_i = word[:i] + word[i+1:]  # Skip i_th character
            # check if we can found any word same as this {skip_i}, so that we can insert i character if needed
            sz = lsc(skip_i) + 1 # +1 for inclusion of this {word}
            cnt = max(cnt, sz)

        cache[word] = cnt 
        return cnt 

    return max([lsc(w) for w in words])


def longestStrChain(words: List[str]) -> int:
    # TODO     
    # define the dp with hash_map and initilize each word in words with possible longest string chain = 1 (itself)	
    dp = {}
    for word in words:
        if word not in dp:
            dp[word] = 1
    # sort the word and work from the shortest ones
    for word in sorted(words, key=len):
        # get all possible substring (sub_word) of current word removing 1 letter
        for i in range(len(word)):
            s = word[:i] + word[i+1:]
            # if the sub_word in dp
            if s in dp:
                dp[word] = max(dp[word], dp[s] + 1)
    return max(dp.values())

