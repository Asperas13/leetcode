class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(0, len(flowerbed)):
            if n == 0:
                break

            if flowerbed[i] == 0:
                if (i - 1 >= 0 and flowerbed[i - 1] == 1) or (i + 1 < len(flowerbed) and flowerbed[i + 1] == 1):
                    continue
                flowerbed[i] = 1
                n -= 1

        return n <= 0