# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack = []
        output = []

        cur_index = 0
        while head:
            output.append(0)
            while stack and stack[-1][0] < head.val:
                elem, index = stack.pop()
                output[index] = head.val

            stack.append((head.val, cur_index))
            cur_index += 1
            head = head.next

        return output