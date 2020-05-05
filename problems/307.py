class SumSegmentTree:
    def __init__(self, array):
        self.array = array
        self.tr = [0] * 4 * len(array)
        if self.array:
            self.__build(0, len(array) - 1, 0)

    def __build(self, lo, hi, pos):
        if lo == hi:
            self.tr[pos] = self.array[lo]
            return

        mid = lo + (hi - lo) // 2
        self.__build(lo, mid, 2 * pos + 1)
        self.__build(mid + 1, hi, 2 * pos + 2)
        self.tr[pos] = self.tr[2 * pos + 1] + self.tr[2 * pos + 2]

    def update(self, index, value):
        if not self.array:
            return
        delta = value - self.array[index]
        self.array[index] = value
        self.__update(0, len(self.array) - 1, index, 0, delta)

    def __update(self, lo, hi, index, pos, delta):
        if index >= lo and index <= hi:
            self.tr[pos] += delta

        if index < lo or index > hi or (index == lo and index == hi):
            return

        mid = lo + (hi - lo) // 2
        self.__update(lo, mid, index, 2 * pos + 1, delta)
        self.__update(mid + 1, hi, index, 2 * pos + 2, delta)

    def query(self, qlo, qhi):
        if not self.array:
            return 0
        return self.__query(qlo, qhi, 0, len(self.array) - 1, 0)

    def __query(self, qlo, qhi, lo, hi, pos):
        if qlo <= lo and hi <= qhi:
            return self.tr[pos]

        if qhi < lo or qlo > hi:
            return 0

        mid = lo + (hi - lo) // 2
        return self.__query(qlo, qhi, lo, mid, 2 * pos + 1) + self.__query(qlo, qhi, mid + 1, hi, 2 * pos + 2)


class NumArray:
    def __init__(self, nums):
        self.tree = SumSegmentTree(nums)

    def update(self, i: int, val: int) -> None:
        self.tree.update(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.tree.query(i, j)


s = NumArray([7,2,7,2,0])
print(1, s.update(4, 6)) # None
print(2, s.update(0, 2))  # None
print(3, s.update(0, 9))  # None
print(4, s.sumRange(4, 4)) # 6
print(5, s.update(3, 8)) # NOne
print(6, s.sumRange(0, 4)) # 32
print(7, s.update(4, 1)) # None
print(8, s.sumRange(0, 3)) # 26
print(9, s.sumRange(0, 4)) # 27

"""
["NumArray","update","update","update","sumRange","update","sumRange","update","sumRange","sumRange","update"]
[[[7,2,7,2,0]],[4,6],[0,2],[0,9],[4,4],[3,8],[0,4],[4,1],[0,3],[0,4],[0,4]]
"""