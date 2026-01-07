from typing import List
from collections import deque
import math

'''
Idea 
0-1 MFS (BFS + DFS) // Hybrid Search
maintain que of candidate as per their cost (ie order by cost to reach to the cell)

It's not pure bfs (despite used queue)
It's not pure dfs (as we add something on left of queue)

It's mixed approach to make things work based on priority 
(ie Custom Algorithm that takes notions from greedy, bfs, dfs, priority queue)
'''


class Solution:
	def minCost(self, grid: List[List[int]]) -> int:
		# 1. prep (resource) ---
		# direction -> offset
		directions = {
			1: (0, 1),  # go to right (axis1)
			2: (0, -1),  # go to left (axis1)
			3: (1, 0),  # go to bottom (axis0)
			4: (-1, 0),  # go to top (axis0)
		}
		rows, cols = len(grid), len(grid[0])
		target = (rows - 1, cols - 1)
		start = (0, 0)
		min_cost_cache = {start: 0}  # (r, c) -> cost

		# 2. data structure ---
		que = deque([(start, 0)])  # (cell, cost)

		while que:
			candidate, cost = que.popleft()  # next cost-effective destination
			if candidate == target:
				# reached destination (as we are employing Greedy Tehcnique we will reach here with min cost)
				return cost
			r, c = candidate
			# try exploring neighbor cells
			for direction, (dr, dc) in directions.items():
				nei = (nr, nc) = r + dr, c + dc

				in_bounds = (0 <= nr < rows) and (0 <= nc < cols)
				if not in_bounds:
					continue

				change_in_direction = direction != grid[r][c]
				cost_to_move = cost + 1 if change_in_direction else cost
				# if visited (nr, nc) earlier, then get that cost
				old_cost = min_cost_cache.get(nei, math.inf)
				if cost_to_move >= old_cost:
					# as new cost to move to (nr, nc) is not fruitful
					continue

				min_cost_cache[nei] = cost_to_move  # remember new better cost

				if change_in_direction:
					# 1 - BFS (ie to right side as it holds some more cost than what present in current at que)
					que.append((nei, cost_to_move))
				else:
					# 0 - BFS (ie to left side as it holds same cost as what present in current que
					# NOTE: this is not pure BFS because we are appending at left side it may not process elements added in order
					# As we append on left it's nature equivalent to stack (ie DFS)
					que.appendleft((nei, cost_to_move))
		return -1
