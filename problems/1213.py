class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        arr1, arr2, arr3 = set(arr1), set(arr2), set(arr3)

        answer = []
        for elem in arr3:
            if elem in arr2 and elem in arr1:
                answer.append(elem)

        return list(sorted(answer))