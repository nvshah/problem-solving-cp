# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/

from typing import List
from itertools import product


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        visited = [[0] * cols for _ in range(rows)]

        def in_bounds(x, y):
            return 0 <= x < rows and 0 <= y < cols

        def dfs(x, y):
            if not in_bounds(x, y):
                return 0
            if grid[x][y] == 0:
                return 0  # non-water cell
            if visited[x][y]:
                return 0

            visited[x][y] = 1

            neighbors = 0
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                neighbors += dfs(nx, ny)

            return grid[x][y] + neighbors

        ans = 0
        for r, c in product(range(rows), range(cols)):
            ans = max(ans, dfs(r, c))

        return ans
