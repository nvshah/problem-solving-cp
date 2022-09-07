# https://leetcode.com/problems/construct-string-from-binary-tree/


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree2str(root: Optional[TreeNode]) -> str:
    def pre(n):
        if not n: return ''
        
        # Raw Parts
        l = pre(n.left) # left
        r = pre(n.right) # right
        
        # Effective parts
        er = f'({r})' if r else ''
        el = f'({l})' if l or r else ''
        
        return f'{n.val}{el}{er}'
    
    return pre(root)

def tree2str2(root):
    s = root.val
    if root.left:
        s += '(' + tree2str2(root.left) + ')'    

    if root.right: 
        if not root.left:
            s += '()'
        s += '(' + tree2str2(root.right) + ')'

    return s  