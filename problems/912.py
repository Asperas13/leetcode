# Counting Sort
"""
class Solution:
    def sortArray(self, nums):
        R = [0 for _ in range(100001)]
        aux = [None for _ in range(100001)]
        for i in nums:
            R[i + 50001] += 1

        for i in range(1, len(R)):
            R[i] += R[i - 1]

        for i in nums:
            ind = R[i + 50000]
            aux[ind] = i
            R[i + 50000] += 1

        return [i for i in aux if i is not None]

"""


# Merge Sort
class Solution:
    def sortArray(self, nums):
        def _sort(nums, l, r, aux):

            if l >= r:
                return nums

            mid = (l + r) // 2

            _sort(nums, l, mid, aux)
            _sort(nums, mid + 1, r, aux)
            _merge(nums, l, mid, r, aux)
            return nums

        def _merge(nums, l, m, r, aux):
            for k in range(l, r + 1):
                aux[k] = nums[k]

            i, j = l, m + 1
            for k in range(l, r + 1):
                if i > m:
                    nums[k] = aux[j]
                    j += 1
                elif j > r:
                    nums[k] = aux[i]
                    i += 1
                elif aux[i] < aux[j]:
                    nums[k] = aux[i]
                    i += 1
                else:
                    nums[k] = aux[j]
                    j += 1

            return nums

        aux = [nums[i] for i in range(len(nums))]
        return _sort(nums, 0, len(nums) - 1, aux)


