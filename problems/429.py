"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import defaultdict


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        nodes_by_level = defaultdict(list)

        def _dfs(node, depth):
            if not node:
                return

            nodes_by_level[depth].append(node.val)

            for child in node.children:
                _dfs(child, depth + 1)

        _dfs(root, 1)
        return nodes_by_level.values()