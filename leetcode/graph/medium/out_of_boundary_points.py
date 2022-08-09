# https://leetcode.com/problems/out-of-boundary-paths/

def findPaths(m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
    cache = {}
    
    def dfs(r, c, movesLeft):
        if r<0 or r==m or c<0 or c==n: return 1
        if not movesLeft: return 0
        
        k = (r, c, movesLeft)
        if k in cache: return cache[k]
        
        left = dfs(r, c-1, movesLeft-1)
        right = dfs(r, c+1, movesLeft-1)
        up = dfs(r-1, c, movesLeft-1)
        down = dfs(r+1, c, movesLeft-1)
        
        v = left + right + up + down
        cache[k] = v
        
        return v
    
    return dfs(startRow, startColumn, maxMove) % (10**9 + 7)
