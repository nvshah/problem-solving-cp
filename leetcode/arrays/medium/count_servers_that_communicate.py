# https://leetcode.com/problems/count-servers-that-communicate

from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        horizontal_counts = [0] * cols
        vertical_counts = [0] * rows

        # preprocessing
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    horizontal_counts[j] += 1
                    vertical_counts[i] += 1

        ans = 0
        for i in range(rows):
            for j in range(cols):

                if not grid[i][j]:
                    continue

                can_talk = max(horizontal_counts[j], vertical_counts[i]) > 1
                if can_talk:
                    ans += 1
        return ans
