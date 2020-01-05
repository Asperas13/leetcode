# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow = head
        fast = head
        while True:
            slow = slow.next
            fast = fast.next
            if not fast or not fast.next:
                return False
            fast = fast.next
            if fast is slow:
                return True
