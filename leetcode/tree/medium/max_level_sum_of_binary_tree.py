# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree?envType=daily-question&envId=2026-01-06
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, ans, cur_level = float("-inf"), 0, 1
        queue = deque([root])

        while queue:
            next_items = []
            curr_sum = 0  # sum of current level

            # prepare next level
            for _ in range(len(queue)):
                node = queue.popleft()
                curr_sum += node.val
                if node.left:
                    next_items.append(node.left)
                if node.right:
                    next_items.append(node.right)

            if curr_sum > max_sum:
                max_sum, ans = curr_sum, cur_level

            # move to next level
            cur_level += 1
            queue.extend(next_items)

        return ans
