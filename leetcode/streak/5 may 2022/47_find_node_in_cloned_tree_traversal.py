# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''Idea : Pre-Order Traversal'''
def getTargetCopy(original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def pre(t1, t2):
            if not t1: return None
            
            if t1 == target:
                return t2
            
            a = pre(t1.left, t2.left)  # left
            if a: return a
            
            a = pre(t1.right, t2.right) # right
            if a: return a
            
            return None
        
        return pre(original, cloned)