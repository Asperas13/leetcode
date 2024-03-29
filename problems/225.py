from queue import Queue


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.queue = Queue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """

        self.queue.put(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """

        top = self.top()
        while True:
            elem = self.queue.get()
            if top == elem:
                break
            self.push(elem)
        return top

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        copy = Queue()

        while not self.empty():
            elem = self.queue.get()
            copy.put(elem)

        self.queue = copy
        return elem

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """

        return self.queue.empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()