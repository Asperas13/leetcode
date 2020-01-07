class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_list_item(self, item):

        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

        return

    def pop_head(self):
        if self.head:
            k = self.head
            if not self.head.next:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

            return k


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.sum = 0
        self.count = 0
        self.ll = SingleLinkedList()
        self.size = size

    def next(self, val: int) -> float:
        self.sum += val
        self.count += 1
        self.ll.add_list_item(val)
        if self.count > self.size:
            node = self.ll.pop_head()
            self.count -= 1
            self.sum -= node.value
        return self.sum / self.count

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)