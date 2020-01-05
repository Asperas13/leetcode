# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_node = ListNode(-1)
        head = result_node
        remains = 0
        while l1 or l2:
            cur = 0
            if l1:
                cur += l1.val
                l1 = l1.next
            if l2:
                cur += l2.val
                l2 = l2.next

            if remains:
                cur += remains

            if cur >= 10:
                remains = cur // 10
                cur = cur - remains * 10
            else:
                remains = 0
            head.next = ListNode(cur)
            head = head.next
        if remains:
            head.next = ListNode(remains)
        return result_node.next
