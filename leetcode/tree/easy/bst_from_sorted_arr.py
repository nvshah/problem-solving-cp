from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    def constructor(l, r):
        '''
        :param l: left pointer
        :param r: right pointer
        '''
        # Edge Case
        if l > r:  # reach to the leaf node so append null as both the child
            return None

        # As array is sorted so middle element of arr is always gona parent/root node
        mid = l + (r-l)//2        
        parent = TreeNode(nums[mid])
        parent.left = constructor(l, mid-1) # left part (BST) recursively
        parent.right = constructor(l, mid+1) # right part (BST) recursively

        return parent # return parent once left & right part is created
    return constructor(0, len(nums)-1)




