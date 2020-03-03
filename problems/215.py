from random import randint


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot_index = randint(0, len(nums) - 1)
        pivot = nums[pivot_index]
        left = [nums[i] for i in range(len(nums)) if i != pivot_index and nums[i] > pivot]
        right = [nums[i] for i in range(len(nums)) if i != pivot_index and nums[i] <= pivot]

        index_of_pivot = len(left)

        if index_of_pivot > k - 1:
            return self.findKthLargest(left, k)
        elif index_of_pivot < k - 1:
            return self.findKthLargest(right, k - index_of_pivot - 1)
        else:
            return pivot
