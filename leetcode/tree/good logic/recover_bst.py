# https://leetcode.com/problems/recover-binary-search-tree/
from typing import Optional
import itertools as it
import operator as op

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rectifyArray(a, key):
    ''' ReCorrect the sorted order of array {a} by rectifying the correct loc of 2 misplaced elem '''
    #s = enumerate(it.pairwise(a))
    def pred(idx):  # check for sorted order
        c, n = key(a[idx]), key(a[idx+1])
        return c < n

    s = iter(range(len(a))) 
    f = it.dropwhile(pred, s)  # Find first incorrect loc
    l = next(f)  # first incorrect location is ensured
    t = it.dropwhile(pred, s) # Find second incorrect loc
    e = next(t, None)  # second incorrect location may not be found
    r = e + 1 if e else l+1

    return l, r

def recoverTree(root: Optional[TreeNode]) -> None:
    
    # 1. get partially sorted order
    inorder = []
    def dfs(n):
        if not n: return
        dfs(n.left)
        inorder.append(n)
        dfs(n.right)
    
    # find 2 incorrect location
    l, r = rectifyArray(inorder, op.attrgetter('val'))

    # 3. Swap 2 incorrect places
    n1, n2 = inorder[l], inorder[r]
    n1.val, n2.val = n2.val, n1.val


def fixSorting(a):
    # find 2 incorrect location
    l, r = 0, len(a)-1
    while l < r:
        if a[l] > a[r]:
            break 
        l += 1
    
    while l < r:
        if a[l] > a[r]:
            break 
        r -= 1
    
    # 3. Swap 2 incorrect places
    a[r], a[l] = a[l], a[r]




