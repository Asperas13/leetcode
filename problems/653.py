# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False

        stack = [root]
        root_copy = root

        def _find(node, target, first_node):
            while node:
                if node.val == target and first_node is not node:
                    return True
                elif node.val < target:
                    node = node.right
                else:
                    node = node.left
            return False

        while stack:
            node = stack.pop()
            if _find(root_copy, k - node.val, node):
                return True

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return False