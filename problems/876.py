# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        val1 = head

        while head.next:
            val1 = val1.next
            head = head.next
            if head.next:
                head = head.next
        return val1

