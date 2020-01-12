# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        n = 0
        while True:
            if root is not None:
                stack.append(root)
                root = root.left

            elif stack:
                root = stack.pop()
                n += 1
                if n == k:
                    return root.val

                root = root.right
            else:
                break

        return -1
