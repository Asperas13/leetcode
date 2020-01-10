# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def _inorder(node, result):
            if node:
                if node.left:
                    _inorder(node.left, result)

                result.append(node.val)

                if node.right:
                    _inorder(node.right, result)

        result = []
        _inorder(root, result)
        return result