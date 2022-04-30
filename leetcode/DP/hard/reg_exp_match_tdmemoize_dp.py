# https://leetcode.com/problems/regular-expression-matching/

def isMatch(s: str, p: str) -> bool:
    len_s = len(s)
    len_p = len(p)

    cache = {}  # Memoization

    def dfs(i, j):
        
        ''' i :- index for string {s}  // string
            j :- index for string {p}  // pattern
        '''
        if (i, j) in cache: return cache[(i,j)]

        s_exhaust = i == len_s
        p_exhaust = j == len_p
        if s_exhaust and p_exhaust:  # Both String & Pattern Consume entirely matching each character at resp positions
            return True 
        
        if p_exhaust:
            return False  # as some pattern is missing

        # check if char at {i} in {s} is same as {j} in {p}
        match = (not s_exhaust) and (p[j] in (s[i], '.')) 

        res = False 

        # check for neighbor `*`
        if (j+1 < len_p) and p[j+1] == '*':
            res = (dfs(i, j+2)  or     # 1. don't use (ie ignore) '*'
                    (match and dfs(i+1, j)))  # 2. use '*' only if current character matches
        elif match:
            res = dfs(i+1, j+1)

        cache[(i,j)] = res        
        return res
    
    return dfs(0, 0)
        

s = "aa"
p = "a"

s = "aa"
p = "a*"

s = 'ab'
p = '.*'

ans = isMatch(s, p)
print(ans)

