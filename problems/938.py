# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        range_sum = 0
        if not root:
            return range_sum

        def _traverse(node):
            nonlocal range_sum
            if L <= node.val <= R:
                range_sum += node.val

            if node.left:
                _traverse(node.left)

            if node.right:
                _traverse(node.right)

        _traverse(root)
        return range_sum
