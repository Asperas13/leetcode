from random import randint


class Node:
    def __init__(self, value):
        self.value = value


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key_to_node = {}
        self.nodes = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.key_to_node:
            node = Node(val)
            self.key_to_node[node.value] = node
            self.nodes.append(node)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.key_to_node:
            node = self.key_to_node[val]
            last_node = self.nodes[len(self.nodes) - 1]
            if last_node.value == node.value:
                self.key_to_node.pop(val)
                self.nodes.pop()
            else:
                last_node_key = last_node.value
                node.value, last_node.value = last_node.value, node.value
                self.nodes.pop()
                self.key_to_node.pop(val)
                self.key_to_node[node.value] = node
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.nodes:
            index = randint(0, len(self.nodes) - 1)
            return self.nodes[index].value

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()