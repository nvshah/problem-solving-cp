# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
from collections import defaultdict

from typing import Optional
from functools import partial
from operator import and_

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def pseudoPalindromicPaths(root: Optional[TreeNode]) -> int:
    def dfs(node, counter):
        if not node:
            return 0
        
        if node.val in counter:
            counter.remove(node.val)
        else:
            counter.add(node.val)
        
        if not node.left and not node.right:
            return 1 if len(counter) <= 1 else 0

        return dfs(node.left, set(counter)) + dfs(node.right, set(counter))

    return dfs(root, set())

def pseudoPalindromicPaths2 (root: Optional[TreeNode]) -> int:
    ans = 0
    counter = defaultdict(int)  # count of each node
    def dfs(node):
        nonlocal ans
        if not node: return
        counter[node.val] += 1  # explore
        
        if not node.left and not node.right:  # leaf node
            i = filter(partial(and_, 1), counter.values())  # get all odd counts
            next(i, None)  # skip first odd cnt if any
            second = next(i, None) # if second odd cnt exists
            ans += 1 if not second else 0
        else:
            dfs(node.left)
            dfs(node.right)
            
        counter[node.val] -= 1  # backtrack
    dfs(root)
    return ans
    
