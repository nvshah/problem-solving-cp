# https://leetcode.com/problems/path-sum-ii/

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(node, total):
            if not node: return 
            path.append(node.val)
            total += node.val

            if not(node.left or node.right):  # Leaf Node
                if targetSum == total: ans.append(path.copy())  
            else:
                dfs(node.left, total)
                dfs(node.right, total)
            
            path.pop()
            total -= node.val

        dfs(root, 0)
        return ans