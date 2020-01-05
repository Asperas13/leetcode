# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return True if not t else False

        def _is_equal(node1, node2):
            if not node1 and not node2:
                return True

            if (node1 and not node2) or (not node1 and node2) or node1.val != node2.val:
                return False

            return _is_equal(node1.left, node2.left) is True and _is_equal(node1.right, node2.right) is True

        stack = [s]
        while stack:
            node = stack.pop()
            if not node:
                continue

            if node.val == t.val and _is_equal(node, t):
                return True

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return False