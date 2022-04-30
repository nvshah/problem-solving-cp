# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional
from collections import deque

#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    '''Via DFS - recursion'''

    def dfs_rec(root):
        if not root: # reach the leaf node
            return 0
        return 1 + max(maxDepth(root.left), maxDepth(root.right))

    def bfs_queue(root):
        ''' BFS via Queue ie counting numbers of levels '''
        if not root:
            return 0
        
        que = deque([root])
        level = 0  # keep track how many levels traversed by (initally none of level is traveresd)

        while que: # keep going till {que} is empty
            # remove all the element that gonna be present at current level from {que}

            for _ in range(len(que)):# traverese entire possible curr level
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            
            level += 1 #  numbers of level traveresed till now
        
        return level

    def dfs_stack(root):
        ''' DFS using stack where stack will hold record ie (node, depth_of_node) 
            We will traverese till we find node with max depth
            Pre-Order Traversel ie Parent -> Left -> Right
        '''
        stack = [(root, 1)] # if root node is present then its depth will be 1
        tree_depth = 0 # depth of tree

        while stack:
            node, depth = stack.pop()

            if node: # if there is node then process it
                # update the depth of tree
                tree_depth = max(tree_depth, depth)
                # check for next level of depth ie {depth+1}
                r = (node.right, depth+1)
                l = (node.left, depth+1)
                stack.extend([r, l]) # so that left is processed first than right

        return tree_depth

    return dfs_rec(root)
