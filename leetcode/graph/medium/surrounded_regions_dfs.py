# https://leetcode.com/problems/surrounded-regions/
from typing import List
from itertools import product, chain

def solve(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # IDEA :- REVERSE THINKING
    #         Start from All boundaries as all boundaries are unsurrounded immplicitly

    m, n = len(board), len(board[0])  # row, col
    
    def markExpose(r, c):
        ''' 
        Idea :- (Reverse Thinking) | DFS
        Find those cells which are not surrounded completely by 'X'
        ie the cells which are exposed to 'X' 
        & mark them with 'E' temporary as a Flag of `Exposed`
        NOTE :- All the boundaries cells are implicitly unSurrounded as there is 1 Missing Side at all 
        
        the region that is explored by this methods remains un-captured in final ans (ie no conversion from 'O' -> 'X')
        '''
        if not ((0 <= r < m) and (0 <= c < n)):  # eddge Cases
            return 

        if board[r][c] == 'O':
            board[r][c] = 'E'  # mark this as un-surrounded (ie Exposed):- 'E'

            # Explore all possible un-surrounded neighbors which not gonna be captured
            markExpose(r-1, c) # TOp
            markExpose(r, c+1) # Right
            markExpose(r+1, c) # Bottom
            markExpose(r, c-1) # left

    # 1. Find all Un-Surrouded cells (from boundaries)
    #   Boundaries :- Row :- [1,m] & Col :- [1,n]

    h = product((0, m-1), range(n))  # Horizontal - Rows as Boundary
    v = product(range(m), (0, n-1))  # Vertical - cols as Boundary

    bounds = chain(h, v)  # 4 boundaries

    for i,j in bounds:  # visit all boundary cells
        markExpose(i,j)

    # 2. Capture the eligible Cells & Undo the Exposed one
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'E':
                board[i][j] = 'O'



def solve2(board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    # IDEA :- REVERSE THINKING
    #         Start from All boundaries as all boundaries are unsurrounded immplicitly

    m, n = len(board), len(board[0])  # row, col

    # 0. Padding board with safe boundaries inorder to avoid edge cases
    pBoard = [
        ['X']*(n+2), 
        *[['X', *board[i], 'X'] for i in range(m)],
        ['X']*(n+2)
    ]
    
    def markExpose(r, c):
        ''' 
        Idea :- (Reverse Thinking)
        Find those cells which are not surrounded completely by 'X'
        ie the cells which are exposed to 'X' 
        & mark them with 'E' temporary as a Flag of `Exposed`
        NOTE :- All the boundaries cells are implicitly unSurrounded as there is 1 Missing Side at all 
        
        the region that is explored by this methods remains un-captured in final ans (ie no conversion from 'O' -> 'X')
        '''
        # if not (0 <= r < m and 0 <= c < n):
        #     return 
        if pBoard[r][c] == 'O':
            pBoard[r][c] = 'E'  # mark this as un-surrounded (ie Exposed):- 'E'

            # Explore all possible un-surrounded neighbors which not gonna be captured
            markExpose(r-1, c) # TOp
            markExpose(r, c+1) # Right
            markExpose(r+1, c) # Bottom
            markExpose(r, c-1) # left

    # 1. Find all Un-Surrouded cells (from boundaries)
    #   Boundaries :- Row :- [1,m] & Col :- [1,n]

    h = product((1, m), range(1, n+1))  # Horizontal - Rows as Boundary
    v = product(range(1, m+1), (1, n))  # Vertical - cols as Boundary

    bounds = chain(h, v)

    for i,j in bounds:
        markExpose(i,j)

    # 2. Capture the eligible Cells & Undo the Exposed one
    for i in range(1, m+1):
        for j in range(1, n+1):
            if pBoard[i][j] == 'O':
                board[i-1][j-1] = 'X'
            elif pBoard[i][j] == 'E':
                board[i-1][j-1] = 'O'





board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
solve(board)
print(board)