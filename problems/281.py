class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.i = 0
        self.j = 0
        self.v1 = v1
        self.v2 = v2
        self.v1_now = True

    def next(self) -> int:
        if self.v1_now:
            if self.i >= len(self.v1):
                current = self.v2[self.j]
                self.j += 1
            else:
                current = self.v1[self.i]
                self.i += 1
                self.v1_now = not self.v1_now
        else:
            if self.j >= len(self.v2):
                current = self.v1[self.i]
                self.i += 1
            else:
                current = self.v2[self.j]
                self.j += 1
                self.v1_now = not self.v1_now
        return current

    def hasNext(self) -> bool:
        return self.i < len(self.v1) or self.j < len(self.v2)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())