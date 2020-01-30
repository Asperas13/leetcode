class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head.next or m == n:
            return head

        cur = 1
        prev = None
        node = head
        while cur < m:
            prev = node
            node = node.next
            cur += 1

        tail, start = node, prev

        while cur <= n:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
            cur += 1

        if start:
            start.next = prev
        else:
            head = prev
        tail.next = node
        return head
