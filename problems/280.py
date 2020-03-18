from heapq import heappush, heappop


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        min_heap, max_heap = [], []
        for i in range(len(nums)):
            heappush(min_heap, nums[i]), heappush(max_heap, -nums[i])

        for i in range(len(nums)):
            if i & 1 == 0:
                nums[i] = heappop(min_heap)
            else:
                nums[i] = -heappop(max_heap)