# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    '''
        max diameter = longest path between 2 nodes in a tree

        Idea : for any node in tree, the longest diameter can be found as
               left sub tree depth to right subtree depth
        
        via Bottom Up Approach 
    '''
    ans = [0] # initially diameter is 0

    # Note :- Leaf denotes the surface

    def depth(node):
        ''' 
            DFS - Bottom UP
            O(n) : as its following bottom up approach so every node will be visited single time only 
        '''
        if not node: # Underground
            return -1 # child of leaf node do not have height as those are underground ie -1
        
        depth_left_part = depth(node.left)
        depth_right_part = depth(node.right)

        # max diameter possible considering current {node} as root node
        diam = depth_left_part + depth_right_part + 2 # 2 for 2 edges connecting left & right part from curret {node}

        ans[0] = max(ans[0], diam)  # little hack as to avoid defining ans as local variable over here

        # depth of current node is :=  1 + (max depth of its children)
        depth_of_node = 1 + depth_left_part + depth_right_part
        return depth_of_node



