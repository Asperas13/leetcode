# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.s = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path(root)
        return self.s

    def max_path(self, node):
        if not node:
            return 0

        left_path_sum = max(self.max_path(node.left), 0)
        right_path_sum = max(self.max_path(node.right), 0)

        self.s = max(self.s, node.val + left_path_sum + right_path_sum, node.val + max(left_path_sum, right_path_sum))

        return node.val + max(left_path_sum, right_path_sum)