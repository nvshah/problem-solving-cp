# https://leetcode.com/problems/binary-tree-postorder-traversal/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    post = []

    def dfs(n):
        if not n: return 
        # 1. Right Child 
        dfs(n.left)
        # 2. Left Child 
        dfs(n.right)
        # 3. Current Node 
        post.append(n.val)
    
    dfs(root)
    return post

def postorderTraversal2(root: Optional[TreeNode]) -> List[int]:
    '''Iterative
    Idea: add node to res when that node is visited second time
    '''
    stack = [root]
    visit = [False] # corresp to stack = define if node is visited 2nd time or not
    res = []

    while stack: 
        cur = stack.pop()
        visitedTwice = visit.pop() 
        if cur:
            if visitedTwice:
                res.append(cur.val)
            else:
                stack.append(cur)  # mark [cur] as ready for result
                visit.append(True) # hence marked True (ie visited twice)

                stack.append(cur.right) 
                visit.append(False) 

                stack.append(cur.left) 
                visit.append(False) 
                
    return res 