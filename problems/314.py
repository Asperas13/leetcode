# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""

from collections import defaultdict, deque


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        column_to_nodes = defaultdict(list)

        def _recurse(node, column):
            if not node:
                return

            column_to_nodes[column].append(node.val)
            _recurse(node.left, column - 1)
            _recurse(node.right, column + 1)

        _recurse(root, 0)
        return column_to_nodes.values()
"""

from collections import defaultdict, deque


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        column_to_nodes = defaultdict(list)
        min_column, max_column = 0, 0
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            column_to_nodes[column].append(node.val)
            min_column = min(min_column, column)
            max_column = max(max_column, column)

            if node.left:
                queue.append((node.left, column - 1))

            if node.right:
                queue.append((node.right, column + 1))

        answer = []
        for i in range(min_column, max_column + 1):
            if column_to_nodes[i]:
                answer.append(column_to_nodes[i])

        return answer