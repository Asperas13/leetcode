"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = deque([(root, 1)])
        prev, prev_depth = None, 0
        while queue:
            node, depth = queue.popleft()

            if depth == prev_depth:
                prev.next = node

            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))

            prev, prev_depth = node, depth

        return root