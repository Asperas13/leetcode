# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        memo = {}

        while headA or headB:
            if headA:
                if headA in memo:
                    return headA

                memo[headA] = 1
                headA = headA.next

            if headB:
                if headB in memo:
                    return headB

                memo[headB] = 1
                headB = headB.next

        return None
