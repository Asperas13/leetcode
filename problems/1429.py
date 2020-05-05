class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = self.tail = None

    def push_back(self, val):
        new_node = ListNode(val)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = self.tail.next

        return new_node

    def push_front(self, val):
        new_node = ListNode(val)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = self.head.prev

        return new_node

    def remove(self, node: ListNode):
        if node is self.head and node is self.tail:
            self.tail = self.head = None
        elif node is self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.text = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def front(self):
        return self.head.val if self.head else None

    def back(self):
        return self.tail.val if self.tail else None

    def is_empty(self):
        return self.head is None


class FirstUnique:
    def __init__(self, nums: List[int]):
        self.dll = DoubleLinkedList()
        self.unique = {}
        self.not_unique = set()
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        if self.dll.front():
            return self.dll.front()
        return -1

    def add(self, value: int) -> None:
        if value in self.unique:
            self.dll.remove(self.unique[value])
            self.not_unique.add(value)
            self.unique.pop(value)
        else:
            if value not in self.not_unique:
                node = self.dll.push_back(value)
                self.unique[value] = node

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)