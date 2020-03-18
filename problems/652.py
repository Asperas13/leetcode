# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import Counter


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        visited = Counter()
        result = []

        def _visit(node):
            if not node:
                return '#'

            s = '%s,%s,%s' % (node.val, _visit(node.left), _visit(node.right))
            visited[s] += 1
            if visited[s] == 2:
                result.append(node)
            return s

        _visit(root)
        return result