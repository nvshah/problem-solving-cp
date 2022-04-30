# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pv = p.val
        qv = q.val
        def find(n):
            # if not n :
            #     return None
            v = n.val
            
            if (pv <= v and qv >= v) or (qv <= v and pv >= v):  # current node {n} is the lca
                return n

            if pv < v and qv < v:    # lca lies in left sub-tree
                return find(n.left)
            else:
                return find(n.right) # lca lies in right sub-tree

        return find(root) 


    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pv = p.val
        qv = q.val
        
        curr = root 

        while curr:
            v = curr.val
            if pv > v and qv > v:  # LCA lies on RHS
                curr = curr.right
            elif pv < v and qv < v:  # LCA lies on LHS
                curr = curr.left
            else:                  # curr node is LCA
                return curr

    def lowestCommonAncestor3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pv = p.val
        qv = q.val
        def find(n):
            v = n.val
            if pv < v and qv < v:    # lca lies in left sub-tree
                return find(n.left)
            elif pv > v and qv > v: # lca lies in right sub-tree
                return find(n.right)
            else:
                return n

        return find(root) 