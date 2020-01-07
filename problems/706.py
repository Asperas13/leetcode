class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 500
        self.map = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        for elem in self.map[index]:
            if elem.key == key:
                elem.value = value
                break
        else:
            self.map[index].append(Node(key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        for elem in self.map[index]:
            if elem.key == key:
                return elem.value

        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        last_elem = len(self.map[index]) - 1
        for i in range(len(self.map[index])):
            if self.map[index][i].key == key:
                self.map[index][i], self.map[index][last_elem] = self.map[index][last_elem], self.map[index][i]
                self.map[index].pop()
                break
        return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)