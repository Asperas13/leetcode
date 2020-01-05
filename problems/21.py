# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        l3 = dummy
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    l3.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    l3.next = ListNode(l2.val)
                    l2 = l2.next
            elif l1:
                l3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                l3.next = ListNode(l2.val)
                l2 = l2.next
            l3 = l3.next

        return dummy.next