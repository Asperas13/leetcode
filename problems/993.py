# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_depth, x_parent = None, None
        y_depth, y_parent = None, None

        def dfs(node, parent, depth):
            nonlocal x_depth, x_parent, y_depth, y_parent
            if not node or (x_depth is not None and y_depth is not None):
                return

            if node.val == x:
                x_depth = depth
                x_parent = parent
            if node.val == y:
                y_depth = depth
                y_parent = parent

            return dfs(node.left, node, depth + 1) or dfs(node.right, node, depth + 1)

        dfs(root, None, 0)
        return x_depth == y_depth and not (x_parent is y_parent)