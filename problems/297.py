# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
queue: [5] serialized: []
queue: [2, 3] serialized [5]
queue: [3, null, null], serialized [5, 2]
queue: [null, null, 2, 4] serialized [5, 2, 3]
queue: [null, 2, 4] serialized [5, 2, 3, null]
queue: [2, 4] serialized [5, 2, 3, null, null]
queue: [4, 3, 1] serialized [5, 2, 3, null, null, 2]
queue: [3, 1, null, null, null, null] serialized [5, 2, 3, null, null, 2, 4]
serialized: [5, 2, 3, null, null, 2, 4, 3, 1, null, null, null, null, null, null, null, null]



                   5
                /     \
               2       3
             /  \     /  \
        null   null  2    4
                    / \
                   3   1

_deserialized


"""

from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        queue = deque()
        queue.append(root)

        serialized = []
        while queue:
            node = queue.popleft()
            if isinstance(node, TreeNode):
                serialized.append(str(node.val))
                queue.extend([node.left, node.right])
            else:
                serialized.append('null')

        return ' '.join(serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = deque(data.split(' '))
        root = TreeNode(int(data.popleft()))
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            if not node:
                continue

            left_child = data.popleft()
            right_child = data.popleft()
            node.left = TreeNode(int(left_child)) if left_child != 'null' else None
            if node.left:
                queue.append(node.left)

            node.right = TreeNode(int(right_child)) if right_child != 'null' else None
            if node.right:
                queue.append(node.right)

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))