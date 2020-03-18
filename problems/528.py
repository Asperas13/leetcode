from random import randint


class Solution:

    def __init__(self, w):
        self.tot = 0
        self.w = []
        for n in w:
            self.tot += n
            self.w.append(self.tot)

    def pickIndex(self) -> int:
        next_int = randint(0, self.tot)

        lo, hi = 0, len(self.w) - 1
        while lo != hi:
            mid = lo + ((hi - lo) // 2)
            if next_int >= self.w[mid]:
                lo = mid + 1
            else:
                hi = mid

        return lo

s = Solution([1, 3])
for i in range(10):
    print(s.pickIndex())