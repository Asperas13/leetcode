# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque, defaultdict


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        nodes = defaultdict(list)
        queue = deque()
        if not root:
            return nodes

        queue.append((root, 0))
        left_to_right = False
        tmp = []

        while queue or tmp:
            node, step = queue.popleft()
            nodes[step].append(node.val)

            if node.left:
                tmp.append((node.left, step + 1))

            if node.right:
                tmp.append((node.right, step + 1))

            if not queue:
                for i in tmp:
                    if not left_to_right:
                        queue.appendleft(i)
                    else:
                        queue.append(i)

                left_to_right = not left_to_right
                tmp = []

        return nodes.values()
