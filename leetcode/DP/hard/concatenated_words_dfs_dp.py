

from typing import List

'''IDEA
- DFS, Recursion, DP

How DFS is related to this Recursion problem ??
-> As for each word we try to rule out via prefix & suffix
   So it will create numerous options of possibility of different pieces of word-stack
   
   prefix - suffix
             |
             prefix - suffix
                        |
                        prefix - suffix
                                  ... 
                                 prefix (ie last piece of entire word)

'''

def findAllConcatenatedWordsInADict(words: List[str]) -> List[str]:
    domain = set(words)  # set of all words (standalone + composed), available at hand
    cache = {} # memoize -> word is composited or not

    def dfs(word): # isABlendOfWords
        '''DFS (Recursion):- Break [word] Till doesnt reach standalone word'''
        if word in cache:
            return cache[word] # Its a solo word
        
        # try to rule out different combinations of chunks/pieces of possibly sub-word
        for i in range(1, len(word)):
            pre, suf = word[:i], word[i:]
            if pre in domain and (suf in domain or dfs(suf)):
                cache[word] = True
                return True
        cache[word] = False
        return False

    return [w for w in words if(dfs(w))]

