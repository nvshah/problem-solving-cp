# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


def flatten(root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """

    #! AIm :- find the right tail for the current root as we need to shift all things on right side

    if not root:
        return None

    head_left, head_right = root.left, root.right
    tail_left, tail_right = None, root

    if head_left:  # if left part exists
        tail_left = flatten(head_left)  # get the tail of left-part
        root.right, root.left = head_left, None  # shift the left inbetween the root & its right part
        tail_right = tail_left  # update current right tail of the root

    if head_right: # if right part exists
        if tail_left:  # bridge between left part & right part ie tail of left to head of right
            tail_left.right = head_right
        tail_right = flatten(head_right) # find the tail of right part

    return tail_right

    