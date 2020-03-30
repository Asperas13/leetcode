# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        height = 1
        node = root
        while node.left:
            node = node.left
            height += 1

        cur_max = node.val
        lo, hi = node.val, 2 ** height - 1  # lo=4, hi=7

        def exists(node, steps):
            for direction in reversed(steps):
                if not node:
                    return False

                if direction == 0:
                    node = node.left
                else:
                    node = node.right

            return True if node else False

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            steps = []
            node_to_check = mid
            while node_to_check > 1:  # mid [1, 0]
                steps.append(node_to_check % 2)
                node_to_check //= 2

            if exists(root, steps):
                cur_max = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return cur_max