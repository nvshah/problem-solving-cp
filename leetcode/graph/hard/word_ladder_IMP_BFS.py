# https://leetcode.com/problems/word-ladder/
from typing import List
from collections import defaultdict, deque

'''
QUe
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

'''

'''
n :- # words
m :- length of each word

'''


def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    '''
    Idea :- BFS -> 
    '''
    if endWord not in wordList:
        return 0  # as there is no path to endWord (ie target) from beginWord
    
    # 1. Create a function to get permut of word
    def get_permut(word):
        ''' get list of permutation that can be possible from word 
        (ie with 1 char difference allowed) 

        O(m) // m := lenght of word

        NOTE :- '*' is used for any character

        Eg :- 'she' :- ['*he', 's*e', 'sh*']
        '''
        
        return (word[:i] + '*' + word[i+1:] for i in range(len(word)))

    # 2. Create Map for pattern -> List[word] // O(n*m^2)
    #        /-> (ie lst of words belonging to that pattern category )
    #             ie all words in lst will be those one that differ by single letter with else other)

    patWords = defaultdict(list)  # pattern -> words
    for w in wordList:
        # 2.1 get all possible patterns for this word {w}
        pats = get_permut(w)  # O(m)
        for p in pats:  
            patWords[p].append(w)  # record {w} for its corresp pattern {p}   // O(m)
    
    print(patWords)
    
    # 3. Do Simple BFS from beegin till end is encounter
    visited = {beginWord}
    # lvl := # words in shortest path
    #   \
    #   -> How many layers You go down from begin word
    lvl = 1  # 1 := beginWord
    
    # Queu DS is used to track #words at current hand(ie turn)
    que = deque([beginWord])

    # THis below part can be done in 2 ways
    while que:
        
        for _ in range(len(que)):  # explore all words at current layer
            w = que.popleft()  # EXIT

            # 1. check if word is end
            if w == endWord:
                return lvl
        
            # 2. explore neighbors to find endWord (ie find all possible words that may differ by 1 character with this word {w})
            pats = get_permut(w)   # O(m^2*n)
            for p in pats:
                words = patWords[p]  # pat -> [words]
                for nei in words:    # Adjacent Words
                    if nei not in visited:
                        # (VISIT) Explore it in next level 
                        que.append(nei)   # REGISTERED
                        visited.add(nei)  # mark registry
        
        # After explored all words at curr level, Move to next level
        lvl += 1

    return 0 # Unable to reach endWord from beginWord
        
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]


beginWord = "hot"
endWord = "dog"
wordList = ["hot","dog"]

l = ladderLength(beginWord, endWord, wordList)
print(l)