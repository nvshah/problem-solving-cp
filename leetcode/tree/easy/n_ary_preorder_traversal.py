# https://leetcode.com/problems/n-ary-tree-preorder-traversal/submissions/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque
from typing import List


def preorder1(root) -> List[int]:
    ''' DFS (Trivial) '''
    ans = []
    
    def helper(n):  # dfs
        if not n: return

        ans.append(n.val)

        for c in n.children:
            helper(c)
    
    helper(root)
    return ans


def preorder2(root) -> List[int]:
    ''' BFS (Non-Trivial) '''
    q = deque([root])
    ans = []

    while q:
        cand = q.popleft()
        ans.append(cand.val)
        q.extendleft(reversed(cand.children)) # Append at front
    
    return ans