# https://leetcode.com/problems/ones-and-zeroes/
from typing import List

# def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#     def k(s):
#         c1 = s.count("0")
#         c2 = s.count("1")
        
#         if c2 == 0:
#             c2 = len(s)+1
        
#         return (c2, c1, len(s)+1)
    
#     na = list(sorted(map(k, strs)))
#     #print(na)
    
#     res = 0
#     j = 0
#     for o, z, w in na:
#         if n <= 0:
#             if j >= m: break
#             if o != 0 and o < w: continue
#             j += z
#         else:
#             n -= o
#             j += z
#         #print(n, j)
#         res += 1
        
#     if n != 0:
#         return 0
    
#     return res

'''Bottom UP Iterative'''
def findMaxForm(strs: List[str], m: int, n: int) -> int:
    # Matrix Form DP -> Top Down Movement & Bottom Up Feeding
    # row -> #ones  (n)
    # col -> #zeros (m)
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for s in strs:
        ones = s.count("1")  # row boundary
        zeros = s.count("0") # col boundary
        for i in range(n, ones-1, -1):
            for j in range(m, zeros-1, -1):
                dp[i][j] = max(dp[i][j], dp[i-ones][j-zeros]+1)
    
    return dp[m][n]

'''Top Down Recursive'''
def findMaxForm(strs: List[str], m: int, n: int) -> int:
    ''''''
    sz = len(strs)
    cache = {}
    def helper(idx, rOne, rZero):
        if idx == sz: return 0
        if rOne + rZero <= 0: return 0

        k = (idx, rOne, rZero)
        if k in cache: return cache[k]

        # Take
        s = strs[idx]
        ones = s.count("1")
        zeros = s.count("0")
        
        tcnt = 0
        if ones <= rOne and zeros <= rZero:
            # Take
            tcnt = 1 + helper(idx+1, rOne-ones, rZero-zeros)
    
        # Discard
        dcnt = helper(idx+1, rOne, rZero)

        res = max(tcnt, dcnt)
        cache[k] = res  #cache

        return res 
    
    
    return helper(0, n, m)


# def findMaxForm(strs: List[str], m: int, n: int) -> int:
#     ''' Incomplete 
#         This is wrong as its caches the Left -> now (which is not what we needed)
#         We need something in DP from now -> Right (ie End)
#     '''
#     sz = len(strs)
#     cache = {}
#     def helper(idx, rOne, rZero, cnt):
#         if idx == sz: return cnt
#         if (rOne + rZero) <= 0: return cnt

#         k = (idx, rOne, rZero)
#         if k in cache: return cache[k]

#         # Take
#         s = strs[idx]
#         ones = s.count("1")
#         zeros = s.count("0")
        
#         tcnt = 0
#         if ones <= rOne and zeros <= rZero:
#             # Take
#             tcnt = helper(idx+1, rOne-ones, rZero-zeros, cnt+1)
    
#         # Discard
#         dcnt = helper(idx+1, rOne, rZero, cnt)

#         res = max(tcnt, dcnt)
#         cache[k] = res  #cache

#         return res 
    
    
#     return helper(0, n, m, 0)