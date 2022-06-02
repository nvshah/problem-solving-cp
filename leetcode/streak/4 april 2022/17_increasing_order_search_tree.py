# https://leetcode.com/problems/increasing-order-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def increasingBST(root: TreeNode) -> TreeNode:
    head = curr = TreeNode(-1)  # Dummy Node for increasing Tree
    def inorder(n):
        nonlocal curr
        if not n: return
        inorder(n.left)  # 1. Left
        curr.right = TreeNode(n.val)  # 2. current Node 
        curr = curr.right  
        inorder(n.right) # 3. right
    inorder(root)
    return head.right