# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def _is_symmetric(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            elif left.val != right.val:
                return False
            else:
                return _is_symmetric(left.right, right.left) and _is_symmetric(left.left, right.right)

        if not root:
            return True

        return _is_symmetric(root.left, root.right)