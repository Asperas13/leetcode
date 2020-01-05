# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        return self.getLeafValues(root1) == self.getLeafValues(root2)

    def getLeafValues(self, root):
        if not root:
            return []

        if not root.right and not root.left:
            return [root.val]
        else:
            return self.getLeafValues(root.right) + self.getLeafValues(root.left)





