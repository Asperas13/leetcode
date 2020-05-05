# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        bits = []

        while head:
            bits.append(head.val)
            head = head.next

        base10 = 0

        for i in range(len(bits)):
            if bits[i]:
                base10 += 2 ** (len(bits) - i - 1)
        return base10