from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapify(stones)
        # [-1 -1]
        while len(stones) > 1:
            x, y = heappop(stones), heappop(stones)
            if x == y:
                continue

            heappush(stones, x - y)

        return -stones[0] if len(stones) == 1 else 0