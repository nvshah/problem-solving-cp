# https://leetcode.com/problems/house-robber-iii/
from typing import Optional

'''
Problem

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

Soln Idea
 -> DFS + DP
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rob(root: Optional[TreeNode]) -> int:
    def dfs(node):
        ''' 
        :param node :- curr {node} (ie curr house)
        :return :- pair of possible rob amount (a1, a2)  // (withNode, withoutNode)
        search the best robbery for given node {node} in 2 possible ways
            1. Considering {node}
            2. Without Considering {node}

            return pair of possible rob amount ie (ra1, ra2)
            where
            ra1 := rob amount with {node} consideration
            ra2 := rob amount without considering {node}
        '''

        if not node:
            return (0, 0) # reach at base of Tree

        
        leftPair = dfs(node.left)   # robbed amount from left part
        rightPair = dfs(node.right) # robbed amount from right part

        withNode = node.val + leftPair[1] + rightPair[1] # total rob amt with {node}
        withoutNode = max(leftPair) + max(rightPair) # total rob amt without {node}

        return (withNode, withoutNode)
        
    return max(dfs(root))