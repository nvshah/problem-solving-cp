# https://leetcode.com/problems/snakes-and-ladders/

from typing import List
from collections import deque

def snakesAndLadders(board: List[List[int]]) -> int:
    ''' Idea : BFS '''
    n = len(board)

    # 1. Reverse the Board so that bottom row can be at 0th pos & likewise for others
    board.reverse()

    # 2.To get pos in Matrix-Board
    def intToPos(i):
        '''get pos (ie (r,c)) in board for corresp number {i}'''
        # As index is 0-based in python & board start with 1
        # so to sync subtract 1 from each cell number to match with 0-indexing of python
        p = i-1  # 0 based int position
        r, c = divmod(p, n)
        if r % 2 != 0: # For Odd no Row it start from right end
            c = -c-1  # indexing from right -> left side starts with -1 & not 0

        return (r, c)
    
    # 3. BFS
    que = deque([(1, 0)])  # elem := (cell, moves)  // moves := to reach this cell
    # ! NOTE :- {moves} denotes number of layer explored in BFS
    visited = set()  # keep track of visited square/cell

    # total cells := 1 to n
    dices = [*range(1,7)]  # total possibility at each layer of BFS exploration = 6  // dice vals
    while que:
        # 1. peek curr cell standing
        ci, moves = que.popleft()   # curr cell idx, total_jumps
        
        # 2. find next cell
        for d in dices:
            # 2.1 next cell idx 
            ni = ci + d

            # 2.2 Location in matrix for corresp {ci}
            r, c = intToPos(ni)

            # 2.3 check if there is any snake or ladder (ie diversion)
            if (di := board[r][c]) != -1:
                ni = di  # new idx of cell is diverted to further due to snake or ladder

            # 2.4. Check if new cell {ci} is destination
            #      !-> +1 to go to next cell ie {ni}
            if ni == n*n: return moves+1  # moves = #layers explored in BFS
            
            # 2.5 check next cell is visited or not earlier
            if ni not in visited:
                visited.add(ni)
                que.append((ni, moves+1))
        
    # 3. No cell can be found towards destination
    return -1

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
ans = snakesAndLadders(board)
print(ans)










        



