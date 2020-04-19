# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def _recurse(node, is_left):
            total = 0
            if not node:
                return total

            if is_left and not node.left and not node.right:
                total += node.val

            return total + _recurse(node.left, True) + _recurse(node.right, False)

        return _recurse(root, False)
