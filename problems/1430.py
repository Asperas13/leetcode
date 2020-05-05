# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def recurse(node, i):
            if not node or node.val != arr[i]:
                return False

            if i == len(arr) - 1:
                if not node.left and not node.right:
                    return True
                return False

            return recurse(node.left, i + 1) or recurse(node.right, i + 1)

        return recurse(root, 0)