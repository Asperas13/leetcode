class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        def _merge(l1, l2):
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

        i = 0
        while len(lists) > 1:
            lists[i] = _merge(lists[i], lists.pop())
            i += 1
            if i >= len(lists) - 1:
                i = 0

        return lists[0]