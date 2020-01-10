from heapq import heappush, heappop, heappushpop

# (1, 1)
# (2, 2)
# (3, 3)
# (4, 4)
# (5, 5)
# (6, 6)
# (7, 7)
# (8, 8)


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def _binary_search(self, num):

        lo, hi = 0, len(self.data) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.data[mid] > num:
                hi = mid - 1
            elif self.data[mid] < num:
                lo = mid + 1
            else:
                return mid

        return lo

    def addNum(self, num: int) -> None:
        pos = self._binary_search(num)
        self.data.insert(pos, num)

    def findMedian(self) -> float:
        if len(self.data) == 0:
            return 0
        mid = len(self.data) // 2
        if len(self.data) & 1 == 0:
            return (self.data[mid] + self.data[mid - 1]) / 2
        else:
            return self.data[mid]


if __name__ == '__main__':
    s = MedianFinder()
    for i in [1, 2, 3, 4]:
        s.addNum(i)
        print(s.findMedian())