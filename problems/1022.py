# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def _sum(node, current_representation):
            if not node:
                return 0

            current_representation += str(node.val)
            if not node.left and not node.right:
                grade = 1
                current_sum = 0
                for i in range(len(current_representation) - 1, -1, -1):
                    if current_representation[i] == '1':
                        current_sum += grade
                    grade *= 2
                return current_sum
            else:
                if node.left and node.right:
                    return _sum(node.left, current_representation) + _sum(node.right, current_representation)
                elif node.left:
                    return _sum(node.left, current_representation)
                else:
                    return _sum(node.right, current_representation)

        return _sum(root, '')
