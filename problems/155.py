class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.mins = []
        self.count = 0

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.count:
            self.mins.append(x)
        else:
            self.mins.append(min(self.mins[self.count - 1], x))
        self.count += 1

    def pop(self) -> None:
        if not self.count:
            return None
        else:
            self.stack.pop()
            self.mins.pop()
            self.count -= 1

    def top(self) -> int:
        if not self.count:
            return None
        return self.stack[self.count - 1]

    def getMin(self) -> int:
        if not self.count:
            return None
        return self.mins[self.count - 1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()