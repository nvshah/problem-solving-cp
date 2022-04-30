# https://leetcode.ca/all/269.html
# https://leetcode.com/discuss/interview-question/248131/Alien-Dictionary-for-Microsoft-Interview-(round-1)-Feb-20th-2019

from typing import List
import itertools as it


def alienOrder(words: List[str]) -> str:
    # Relative Ordering of Charcters : character mapping to its successor characters
    adj = {c: set() for word in words for c in word}

    wordLen = len(words)

    for w1, w2 in it.pairwise(words):
        w1Len, w2Len = len(w1), len(w2)
        minLen = min(w1Len, w2Len)

        for i in range(minLen):
            c1, c2 = w1[i], w2[i]
            # if c1 > c2:  # incorrect lexiographic
            #     return ''
            
            if c1 != c2:
                adj[c1].add(c2)  # c1 -> c2
                break
        else:
            # all characters are same (till minLen)
            if w1Len > w2Len: # if w1 is larger than w2 then its incorrect lexiographically
                return ''
        
        
    # character -> bool
    visited = {} # False :- Visited, True :- Visited & in Curr-Path (ie Cyclic Path)

    res = [] # hold all the characters in reveresed order by Topological sort

    print(adj)

    def dfs(c):
        '''
        Do Topological sort (ie Post Order DFS) = to get reversed sorted string
        NOTE :- here it will not sort based on lexiographic order but based on Relative Orderinng of 
                Character defined by {adj} mapping of characters

        return if Cycle Exists or Not during exploration
        '''
        if c in visited:  # if c is visited earlier or not
            return visited[c] # if c is in current path or not

        visited[c] = True

        for nei in adj[c]:  # Neighbor First than parent
            if dfs(nei): 
                return True
        
        visited[c] = False

        res.append(c) # append the {c} to result ie Parent at last ie post order

    for c in adj:
        if dfs(c):    # Cycle Exists
            return ''
    
    return ''.join(reversed(res))

w = [
"wrt",
"wrf",
"er",
"ett",
"rftt"
]

a = alienOrder(w)
print(a)
        
        