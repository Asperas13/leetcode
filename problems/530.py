# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        tree = self.serialize_to_list(root)
        tree.sort()
        return min([abs(tree[i] - tree[i - 1]) for i in range(1, len(tree))])

    def serialize_to_list(self, binary_tree):
        if not hasattr(binary_tree, 'val'):
            return []

        left = self.serialize_to_list(binary_tree.left)
        right = self.serialize_to_list(binary_tree.right)

        return [binary_tree.val] + left + right
