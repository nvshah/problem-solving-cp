from typing import List 

def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    g = obstacleGrid  
    if g[0][0] or g[-1][-1] : return 0  # edge cases
    
    m, n = len(g), len(g[0]) 
    
    # start from last row (ie DP)
    prevRow = [0]*n
    c = n-1
    while c >= 0 and g[-1][c] == 0:  # until no block found
        prevRow[c] = 1
        c -= 1

    for i in range(m-2, -1, -1): # Skipping last row
        last = 1-g[i][-1] if prevRow[-1] else 0  # decide last col val
        currRow = [*([0] * (n-1)), last]
        for j in range(n-2, -1, -1): # starting from last second element (as last elem gonna decide individually as above)
            if g[i][j] != 1:
                right, bottom = currRow[j+1], prevRow[j]
                currRow[j] = right + bottom
                
        prevRow = currRow

    return prevRow[0]

m = [[0,0],[1,1],[0,0]]
m = [[0,0,0],[0,1,0],[0,0,0]]
m = []

a = uniquePathsWithObstacles(m)

print(a)