# https://leetcode.com/problems/binary-search-tree-iterator/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator:

    '''Idea : We will use Stack to store the current node & for traversal in In-Order fashion
        
       NOTE :- at any given time max elements that can lie in stack = O(height_bst) 
              //because max 1 can go from root -> left-most child in linear fashion 
    '''

    def track_down_left(self, node):
        # go till left-most node found
        while node:
            self.stack.append(node)
            node = node.left

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []

        # initialize the stack with bst tree's possible next element at top 
        # Max elem that can lie in stack := O(height_bst)
        
        # go till left-most node found
        self.track_down_left(root)
        

    def next(self) -> int:
        top = self.stack.pop()
        curr = top.right

        # add all elem down the level to {top} node (ie Right Side)
        self.track_down_left(curr)

        return top.val 
        

    def hasNext(self) -> bool:
        return bool(self.stack)