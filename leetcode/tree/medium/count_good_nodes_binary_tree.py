# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

'''
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root: TreeNode) -> int:

    def dfs(node, maxVal):
        '''
        node :- current node
        maxVal :- maximum value in a particular branch of tree fromm {root} -> {node}
        returns :- good node counts for branch {root} -> {node}
        '''
        if not node: return 0 # edge case : reach underground

        # PRE-ORDER Traversal :- Parent -> Left -> Right

        cnt = int(node.val >= maxVal)  # 1 if good node else 0

        maxVal = max(maxVal, node.val) # update maxVal

        cnt += dfs(node.left, maxVal)  # Left SubTree Explore
        cnt += dfs(node.right, maxVal) # Right Subtree Explore

        return cnt  

    return dfs(root, root.val)      


        