# https://leetcode.com/problems/map-of-highest-peak/description/

from typing import List
from collections import deque
from itertools import product


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        que = deque()  # (x, y, height)
        seen = set()  # (i, j)

        rows, cols = len(isWater), len(isWater[0])
        ans = [[-1] * cols for _ in range(rows)]

        # identify water cells

        cell_pos = product(range(rows), range(cols))

        for i, j in cell_pos:
            if isWater[i][j] != 1:
                continue
            que.append((i, j, 0))
            seen.add((i, j))

        # Multi-Source BFS
        while que:
            x, y, height = que.popleft()
            ans[x][y] = height

            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy

                in_bounds = 0 <= nx < rows and 0 <= ny < cols
                if not in_bounds:
                    continue

                if (nx, ny) in seen:
                    continue

                seen.add((nx, ny))
                que.append((nx, ny, height + 1))

        return ans
