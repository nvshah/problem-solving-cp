# https://leetcode.com/problems/find-duplicate-subtrees/
from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findDuplicateSubtrees(root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    reprMap = {} # representation of subtree -> root node of subtree
    res = [] # root of duplicate subtrees
    def pre(node):
        if node is None: return 'N'

        reprLeft = pre(node.left) 
        reprRight = pre(node.right)

        rep = f'{node.val},{reprLeft},{reprRight}'
        roots = reprMap.setdefault(rep, [])
        
        if len(roots) == 1:
            res.append(node) # duplicate

        roots.append(node)
        return rep

    pre(root)
    return res 


        