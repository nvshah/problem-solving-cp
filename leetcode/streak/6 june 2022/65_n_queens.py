# https://leetcode.com/problems/n-queens/


from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    board = [["."] * n for _ in range(n)]

    # Below sets keep tracks of respective acquired columns, pos-diag, neg-diag by Queens
    cols = set()  # columns acquired by queens
    pos_diags = set()  # defined by (r-c)
    neg_diags = set()  # defined by (r+c)

    res = []  # result set keep track of all possible boards

    def backtrack(r):
        if r == n:  # all rows are explored
            snap = ["".join(row) for row in board]  # row -> string
            res.append(snap)
            return

        # Explore each column of current row where Queen can be placed
        for c in range(n):
            # 1. find the positive & negative diagonal number this cell (r, c) belongs to.
            diagP, diagN = r - c, r + c

            # 2. check if an Queen Exists already in any of Column, or Diagonal
            #    (Note : not checking of Row as we are already traversing Row by Row placing single Queen)
            if (c in cols) or (diagN in neg_diags) or (diagP in pos_diags):
                continue  # Queen cannot be placed at (r,c)

            # 3. place Queen at (r,c)
            board[r][c] = "Q"
            #    register acquirance
            cols.add(c)
            pos_diags.add(diagP)
            neg_diags.add(diagN)

            # 4. Explore next row (where Queen can be placed in next Row ??) via Recurssion
            backtrack(r + 1)

            # 5. BackTrack
            #    remove Queen at (r,c)
            board[r][c] = "."
            #    un-register acquirance
            cols.remove(c)
            pos_diags.remove(diagP)
            neg_diags.remove(diagN)

    backtrack(0)  # start fromm first row
    return res
