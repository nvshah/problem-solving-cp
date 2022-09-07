# https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque
from typing import List

def levelOrder(root) -> List[List[int]]:
    if not root: return []
    q = deque([root])
    ans = []
    while q:
        cur = []
        for _ in range(len(q)):
            cand = q.popleft()
            cur.append(cand.val)
            q.extend(cand.children)
        
        ans.append(cur)
    return ans