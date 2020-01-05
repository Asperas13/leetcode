# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        is_palindrome = True
        while is_palindrome and prev:
            if prev.val != head.val:
                is_palindrome = False

            prev = prev.next
            head = head.next

        return is_palindrome