from heapq import heappop, heapify, heappush


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        min_cost = 0

        heapify(sticks)

        while len(sticks) > 1:
            new_stick = heappop(sticks) + heappop(sticks)
            min_cost += (new_stick)
            heappush(sticks, new_stick)

        return min_cost