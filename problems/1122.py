class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        s = {j: i for i, j in enumerate(arr2)}

        l1 = [(s[i], i) for i in arr1 if i in s]
        l2 = [i for i in arr1 if i not in s]

        return [i[1] for i in sorted(l1, key=lambda a: a[0])] + [i for i in sorted(l2)]
