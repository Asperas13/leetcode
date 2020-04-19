from functools import lru_cache


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices == 0 and cheeseSlices == 0:
            return [0, 0]

        if tomatoSlices & 1 == 1 or tomatoSlices < cheeseSlices:
            return []

        x2 = (tomatoSlices - 4 * cheeseSlices) / -2
        x1 = (tomatoSlices - x2 * 2) / 4
        if x1 >= 0 and x2 >= 0:
            return [int(x1), int(x2)]

        return []