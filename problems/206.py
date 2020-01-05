# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        stack = []
        while head:
            stack.append(head)
            head = head.next

        dummy = ListNode(-1)
        head = dummy
        while stack:
            elem = stack.pop()
            head.next = elem
            head = head.next
        head.next = None
        return dummy.next