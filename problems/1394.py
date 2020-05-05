from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)

        lucky = -1
        for num, freq in c.items():
            if num == freq and num > lucky:
                lucky = num

        return lucky