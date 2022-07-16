# https://leetcode.com/problems/interleaving-string/

# APPROACH 1
from pprint import pprint


def isInterleave(s1: str, s2: str, s3: str) -> bool:
    ''' Top-Down Memoizing DP '''
    sz1 = len(s1)
    sz2 = len(s2)
    
    if sz1 + sz2 != len(s3): return False
    
    dp = {} # cache
    # k = i + j  // total skipped characters from {s1, s2}
    # i := s1
    # j := s2
    # k := s3

    def dfs(i, j):
        if i == sz1 and j == sz2:
            return True
    
        key = (i, j)
        if key in dp: return dp[key]
    
        k = i + j  # total accounted characters
    
        # consider from s1
        if i < sz1 and s1[i] == s3[k] and dfs(i+1, j):
            return True
    
        # consider from s2
        if j < sz2 and s2[j] == s3[k] and dfs(i, j+1):
            return True
    
        dp[key] = False
        return False

    return dfs(0, 0)

# APPROACH 2
def isInterleave2(s1: str, s2: str, s3: str) -> bool:   
    '''Bottom Up DP (Matrix-Traditional)'''  
    # APPROACH 2  (Bottom Up)
    n, m = len(s1), len(s2)
    dp = [[False]*(m+1) for _ in range(n+1)]
    dp[n][m] = True  # Bottom Right Corner, ie EOS
    
    for i in range(n, -1, -1):
        for j in range(m, -1, -1):
            if i < n and s1[i] == s3[i+j] and dp[i+1][j]:
                dp[i][j] = True
            elif j < m and s2[j] == s3[i+j] and dp[i][j+1]:
                dp[i][j] = True
    
    return dp[0][0]

# APPROACH 3
def isInterleave3(s1: str, s2: str, s3: str) -> bool:   
    '''Bottom Up DP (Matrix-Traditional)'''  
    '''NEED TO FIX BUG in this CODE'''
    # APPROACH 3  (Bottom Up)
    n, m = len(s1), len(s2)
    dp = [[False]*(m+1) for _ in range(n+1)]
    
    dp[0][0] = True # Empty Strings at both 

    # Col Wise Filling (Empty s1)
    for j in range(1, m+1):
        dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

    # Row Wise Filling (Empty s2)
    for i in range(1, n+1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            t = s3[i+j-1]  # index when we consider either of character from s1 or s2
            if dp[i-1][j] and s1[i-1] == s3[i-1+j]:
                dp[i][j] = True 
            elif dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                dp[i][j] = True 

    pprint(dp)
     
    return dp[n][m]

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

s1 = "a"
s2 = "" 
s3 = "a"

isInterleave3(s1, s2, s3)     
            
            
            