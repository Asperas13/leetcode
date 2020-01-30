# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        node = head
        while prev:
            nxt = node.next
            nxt2 = prev.next
            node.next = prev
            prev.next = nxt
            node = nxt
            prev = nxt2

        if node:
            node.next = None
        return head
