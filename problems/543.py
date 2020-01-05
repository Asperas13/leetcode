# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_height = float('-inf')

        def _height(node):
            nonlocal max_height
            if not node:
                return 0
            elif node.left or node.right:
                left_height = _height(node.left)
                right_height = _height(node.right)
                max_height = max(max_height, 1 + left_height + right_height)
                return 1 + max(left_height, right_height)
            else:
                return 1
        _height(root)
        return max_height - 1 if max_height > float('-inf') else 0