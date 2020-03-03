# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def maxLevelSum(self, root) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])
        max_sum, cur_sum = float('-inf'), 0
        max_level, cur_level = 0, 0
        while queue:
            node, level = queue.popleft()
            if level != cur_level:
                if cur_sum > max_sum:
                    max_sum = cur_sum
                    max_level = cur_level
                cur_level = level
                cur_sum = 0

            cur_sum += node.val

            if node.left:
                queue.append((node.left, cur_level + 1))

            if node.right:
                queue.append((node.right, cur_level + 1))

            if not queue:
                if cur_sum > max_sum:
                    max_level = cur_level

        return max_level
