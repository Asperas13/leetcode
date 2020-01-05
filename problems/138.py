"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def __init__(self):
        self.visited = {}

    def get_visited_node(self, node):
        if node:
            if node in self.visited:
                return self.visited[node]
            else:
                self.visited[node] = Node(node.val, None, None)
                return self.visited[node]

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        old_head = head
        new_head = Node(head.val, None, None)
        self.visited[old_head] = new_head
        while head:
            new_head.next = self.get_visited_node(head.next)
            new_head.random = self.get_visited_node(head.random)

            head = head.next
            new_head = new_head.next

        return self.visited[old_head]