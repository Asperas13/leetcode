from heapq import heappush, heapify, nsmallest


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heappush(heap, (((x ** 2) + (y ** 2)) ** (1 / 2), [x, y]))

        return [i[1] for i in nsmallest(K, heap)]

