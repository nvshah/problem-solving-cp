# Que :- https://leetcode.com/problems/maximal-square/

from typing import List
import itertools as it

''' 
top-down approach for recursice soln

# dynamic programming :- bottum up
# recursive :- top down

'''


def maximalSquare(matrix: List[List[str]]) -> int:
    ''' 
    Recursive Top Down approach
        Time : O(m*n)
        Space : O(m*n)
    '''
    
    ROWS, COLS = len(matrix), len(matrix[0])

    # keep the val for cell if used as top-left Squaare Corner than what is square length possible
    cache = {}  # (r, c) -> maxSquareLength

    def helper(r, c):
        if r >= ROWS or c >= COLS:
            return 0
        
        if (r, c) not in cache:
            # cell is not explored earlier
            
            # explore cell (r, c) as top-left cell for possible square
            down = helper(r+1, c)
            right = helper(r, c+1)
            diag = helper(r+1, c+1)

            cache[(r,c)] = (1 + min(down, right, diag)) if matrix[r][c] == '1' else 0

        return cache[(r,c)]
    
    helper(0, 0) # start computinng entire grid from top-left first cell

    return max(cache.values())**2

def maximalSquareDP2(matrix: List[List[str]]) -> int :
    ''' 
        Time : O(n*m) 
        Idea : Every cell of matrix represent the square possible of length cell-val with that cell as bottom-right cell in that square
    '''
    # use matrix as dp to save space
    ROWS, COLS = len(matrix), len(matrix[0])
    for i in range(ROWS):
        for j in range(COLS):
            if not(i and j):  # for first row & col
                matrix[i][j] = int(matrix[i][j])
                continue
            if matrix[i][j] == '0': # constraints as per problem
                matrix[i][j] = 0
                continue
                
            # explore cell (i, j) as bottom-right cell for possible square
            diagTopLeft = matrix[i-1][j-1]
            top = matrix[i-1][j]
            left = matrix[i][j-1]
            # update matrix aka dp here
            matrix[i][j] = 1 + min(diagTopLeft, top, left)

    return max(it.chain(*matrix))**2

def maximalSquareDP3(matrix: List[List[str]]) -> int :
    ''' 
        Time : O(n*m) 
        Idea : Every Cell as Top-Left
    '''
    # use matrix as dp to save space
    ROWS, COLS = len(matrix), len(matrix[0])
    dp = [[0]*(COLS+1) for _ in range(ROWS+1)]
    side = 0
    for i in range(ROWS):
        for j in range(COLS):
            if matrix[i][j] == '0':
                continue
            # explore cell (i, j) as Top-LEft cell for possible square
            current = dp[i][j]
            bottom = dp[i+1][j]
            right = dp[i][j+1]

            val = dp[i+1][j+1] = 1 + min(current, right, bottom)
            side = max(val, side)
    return side**2

if __name__ == '__main__':
    
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

    ans1 = maximalSquare(matrix)

    print(ans1)

    ans3 = maximalSquareDP3(matrix)
    print(ans3)

    ans2 = maximalSquareDP2(matrix)
    print(ans2)

    








        

