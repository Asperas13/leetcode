# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return root

        closest = None
        closest_distance = float('+inf')

        while root:
            if abs(root.val - target) < closest_distance:
                closest_distance = abs(root.val - target)
                closest = root.val

            if target == root.val:
                return root.val

            elif target > root.val:
                root = root.right

            else:
                root = root.left

        return closest
