# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree?envType=daily-question&envId=2026-01-07

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1:
    def sum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return root.val + self.sum(root.left) + self.sum(root.right)

    def updateMax(self, x: int) -> None:
        self.currentMax = max(self.currentMax, (x * (self.total - x)))

    def dfs(self, node: TreeNode) -> int:
        if node is None:
            return 0
        if node.left is None and node.right is None:
            # leaf node
            self.updateMax(node.val)
            return node.val
        currentSum = node.val + self.dfs(node.left) + self.dfs(node.right)
        self.updateMax(currentSum)
        return currentSum

    def maxProduct(self, root: TreeNode) -> int:
        self.total = self.sum(root)
        self.currentMax = 0
        self.dfs(root.left)
        self.dfs(root.right)
        return self.currentMax % (10**9 + 7)


class Solution2:
    """
    Approach
    1. Collect all subtree sums with a single postorder DFS. Each possible split (removing one edge)
    2. produces subtree sums s and total-s; evaluate s*(total-s) for every subtree and return the maximum.
    (Equivalently, pick the subtree sum closest to total/2.)
    """

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sums = []  # list of sum of all possible sub-trees

        def tree_sum(node):
            """dfs (pre-order tree traversal)
            calculate total sum of tree with root [node]
            """
            if not node:
                return 0
            total = node.val + tree_sum(node.left) + tree_sum(node.right)
            all_sums.append(total)
            return total

        # find sum of all possible sub trees
        total = tree_sum(root)
        # quadratic n*(T-n) is maximized at n = T/2, so pick the list element closest to T/2 (ties give same product)
        # sum1 = min(all_sums, key=lambda n: abs(n - total / 2))
        sum1 = max(all_sums, key=lambda n: n * (total - n))
        sum2 = total - sum1

        return sum1 * sum2
