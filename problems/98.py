class Solution:
    def isValidBST(self, root):
        is_valid = True

        def _validate(node, min_val, max_val):
            nonlocal is_valid
            if not node or not is_valid:
                return

            if node.val <= min_val or node.val >= max_val:
                is_valid = False

            if node.left and node.val <= node.left.val:
                is_valid = False

            if node.right and node.val >= node.right.val:
                is_valid = False

            _validate(node.left, min_val, min(max_val, node.val))
            _validate(node.right, max(min_val, node.val), max_val)

        _validate(root, float("-inf"), float("+inf"))
        return is_valid