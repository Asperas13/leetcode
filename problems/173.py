# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.root = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.root:
            while self.root:
                self.stack.append(self.root)
                self.root = self.root.left

        self.root = self.stack.pop()
        val = self.root.val
        self.root = self.root.right
        return val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.root or self.stack:
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()