# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import defaultdict


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        tree = defaultdict(list)
        stack = [(root, 0)]
        while stack:
            treenode, depth = stack.pop()

            tree[depth].append(treenode.val)

            if treenode.right:
                stack.append((treenode.right, depth + 1))

            if treenode.left:
                stack.append((treenode.left, depth + 1))

        return tree.values()