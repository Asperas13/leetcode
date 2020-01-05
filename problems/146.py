class ListNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self, capacity):
        self._head = None
        self._tail = None
        self._count = 0
        self._capacity = capacity

    def is_empty(self):
        return self._count == 0

    def is_full(self):
        return self._count == self._capacity

    @property
    def count(self):
        return self._count

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def add_node(self, node):
        if self.is_empty():
            self._head = self._tail = node
        else:
            tmp = self._tail
            self._tail = node
            self._tail.prev = tmp
            tmp.next = self._tail
        self._count += 1

    def remove_node(self, node):
        if not self.is_empty():
            if node is self._head:
                if self._head.next:
                    self._head = self._head.next
                    self._head.prev = None
                else:
                    self._head = self._tail = None
            elif node is self._tail:
                if self._tail.prev:
                    self._tail = self._tail.prev
                    self._tail.next = None
                else:
                    self._head = self._tail = None
            else:
                prev = node.prev
                nxt = node.next
                prev.next = nxt
                nxt.prev = prev

            self._count -= 1
            node.next = node.prev = None
            return node


class LRUCache:
    def __init__(self, capacity: int):
        self.key_to_node = {}
        self.dll = DoubleLinkedList(capacity)

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self.dll.remove_node(node)
            self.dll.add_node(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self.dll.remove_node(node)
            self.dll.add_node(node)
        elif self.dll.is_full():
            node = ListNode(key, value)
            self.key_to_node.pop(self.dll.head.key)
            self.dll.remove_node(self.dll.head)
            self.dll.add_node(node)
            self.key_to_node[key] = node
        else:
            node = ListNode(key, value)
            self.dll.add_node(node)
            self.key_to_node[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)