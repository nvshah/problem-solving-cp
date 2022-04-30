# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    ''' Iterative Inorder Traversal 
        Process & Pop
        tree is bST 
    '''
    stack = []
    curr = root
    n = 0

    while curr or stack:
        # process the current node
        while curr:
            # add current node to stack
            stack.append(curr)
            curr = curr.left

        # get the rightmost node ie top at stack (its a smallest elem)
        t = stack.pop()
        n += 1
        if n == k:
            return t.val 

        # Note {t} does not have the left sub-tree as children of it 
        # but it may hold sub-tree on its right side
        
        # explore right part of curr node
        curr = t.right

# def kthSmallest2(root: Optional[TreeNode], k: int) -> int:
#     ''' inorder traversal recursive'''
#     n = [0]
#     def helper(node, cnt):
#         if not node:
#             return cnt
#         # process
#         left_cnt = helper(node.left, cnt)
#         if left_cnt == k:
#             return 
#         n[0] += 1
#         if n == k:
#             return node.val
#         else:
#             helper(node.right)
    
#     return helper(root)

if __name__ == '__main__':

    l2 = TreeNode(2, None, None)
    l1 = TreeNode(1, None, l2)
    l12 = TreeNode(4, None, None)
    root = TreeNode(3, l1, l12)

    ans = kthSmallest(root, 3)
    print(ans)

        
