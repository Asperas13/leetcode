"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def _traverse(node):
            if not node:
                return None

            if node.child and node.next:
                flattened = _traverse(node.child)
                next_to_traverse = node.next
                flattened.next = next_to_traverse
                next_to_traverse.prev = flattened
                node.next = node.child
                node.child.prev = node
                node.child = None
                return _traverse(next_to_traverse)
            elif node.child:
                child = node.child
                node.next = child
                child.prev = node
                node.child = None
                return _traverse(child)
            elif node.next:
                return _traverse(node.next)
            else:
                return node

        _traverse(head)
        return head