# https://leetcode.com/problems/distinct-subsequences/

def numDistinct(s: str, t: str) -> int:
    cache = {}

    def dfs(i, j):
        ''' i :- index of string s
            t :- index of string t
        '''
        if j == len(t):  # target string exhausted
            return 1
        
        if i == len(s): # source string exhausted
            return 0

        if (i,j) in cache:
            return cache[(i,j)]
        
        if s[i] == t[j]:
            v = dfs(i+1, j+1) + dfs(i+1, j)
            cache[(i,j)] = v
        else: 
            dfs(i+1, j)      
         
