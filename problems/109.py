# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        values = []
        while head:
            values.append(head.val)
            head = head.next

        def _construct(l, r):
            if l > r:
                return None

            mid = (l + r) // 2

            root = TreeNode(values[mid])

            root.left = _construct(l, mid - 1)
            root.right = _construct(mid + 1, r)
            return root

        return _construct(0, len(values) - 1)