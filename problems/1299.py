# [18, 18, 6, 6, 6, 1]

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]

        higher = [None] * len(arr)
        higher[-1] = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            higher[i] = max(arr[i], higher[i + 1])

        for i in range(len(arr) - 1):
            arr[i] = higher[i + 1]

        arr[-1] = -1

        return arr