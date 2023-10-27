# https://leetcode.com/problems/construct-quad-tree/description/
from typing import List
from itertools import product, starmap

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)

        def dfs(n, r, c):
            '''n*n size grid with (r,c) as top-left corner'''
            first = grid[r][c]

            indices = product(range(r, r+n), range(c, c+n))
            allElemMatch = starmap(lambda i, j: grid[i][j] == first, indices)
            allSame = all(allElemMatch)
             
            if allSame:
                return Node(first, True)
            
            s = n // 2 # new size
            topLeft = dfs(s, r, c) 
            topRight = dfs(s, r, c+s)
            bottomLeft = dfs(s, r+s, c) 
            bottomRight = dfs(s, r+s, c+s)

            return Node(-1, False, topLeft,topRight, bottomLeft, bottomRight)
        
        return dfs(n, 0, 0)
        