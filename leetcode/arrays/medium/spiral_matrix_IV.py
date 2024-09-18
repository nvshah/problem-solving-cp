# https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        left, right = 0, n - 1
        top, bottom = 0, m - 1

        grid = [[-1] * n for _ in range(m)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # right, down, left, top

        r, c = 0, 0  # current row, col
        cur = head  # traverser
        d = 0  # current direction (for traverser)
        dx, dy = directions[0]  # direction offset (for traverser)

        def change_direction():
            """update dx, dy offset for current direction d"""
            nonlocal d, dx, dy
            d = (d + 1) % 4
            # dx -> horizontal, dy -> vertical
            dx, dy = directions[d]

        def is_in_bound(i, j):
            """check if (i, j) is within boundaries defined by top, right, bottom, left"""
            vertical_constraints = top <= i <= bottom
            horizontal_constraints = left <= j <= right
            return vertical_constraints and horizontal_constraints

        while cur:
            # Fill value
            grid[r][c] = cur.val
            cur = cur.next

            # check if next step is in boundary
            if not is_in_bound(r + dy, c + dx):
                # inorder to avoid repeating of top-left (whilst traversing last direction)
                if d == 0:
                    # first direction
                    # (ie top-border) traversed (hence top-left is accounted)
                    # So shrink just top pointer to next possible top-row
                    top += 1
                elif d == 3:
                    # last direction
                    # hence shrink the boundaries (come inwards)
                    left, right, bottom = left + 1, right - 1, bottom - 1

                change_direction()

            # move ahead
            r, c = r + dy, c + dx

        return grid


m = 3
n = 5
