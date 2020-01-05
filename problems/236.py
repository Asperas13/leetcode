# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def _lca(node, first, second):
            if not node:
                return None

            if node in (first, second):
                return node

            left = _lca(node.left, first, second)
            right = _lca(node.right, first, second)

            if left and right:
                return node

            return left if left is not None else right

        return _lca(root, p, q)