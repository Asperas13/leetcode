# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        if reader.get(0) == target:
            return 0

        lo, hi = 0, 1
        while reader.get(hi) < target:
            lo = hi
            hi *= 2

        if reader.get(hi) == target:
            return hi

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            call_answer = reader.get(mid)
            if call_answer == target:
                return mid
            elif call_answer < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1