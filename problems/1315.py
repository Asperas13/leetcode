class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        def _sum_sons(node):
            if not node:
                return 0
            s = 0
            if node.right:
                s += node.right.val

            if node.left:
                s += node.left.val

            return s

        def _recurse(node):
            total_sum = 0

            if not node:
                return total_sum

            if node.val & 1 == 0:
                total_sum += _sum_sons(node.left)
                total_sum += _sum_sons(node.right)

            return total_sum + _recurse(node.left) + _recurse(node.right)

        return _recurse(root)
