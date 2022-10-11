# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    # O(n) Space + Time
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()

        def dfs(n):
            if not n: return False 
            visited.add(n.val)
            
            if k - n.val in visited:
                return True 
            
            l = dfs(n.left)
            if l: return True 
            r = dfs(n.right)
            if r: return True

            return False

        return self.dfs(root)

class Solution2:
    # O(n) Time
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        def inorder(n):
            if not n: return 
            
            inorder(n.left)
            arr.append(n.val)
            inorder(n.right)

        inorder(root)

        # Traditional way via 2 Pointers for 2 Sum
        l, r = 0, len(arr)-1
        while l < r:
            n1, n2 = arr[l], arr[r]
            t = n1+n2
            if t == k:
                return True
            if t < k:
                l += 1
            else : 
                r -= 1
        return False
