class Solution:
    def searchRange(self, nums, target):

        leftmost_ind = self._binary_search(nums, target, True)
        if leftmost_ind >= len(nums) or nums[leftmost_ind] != target:
            return [-1, -1]

        rightmost_ind = self._binary_search(nums, target, False) - 1
        return [leftmost_ind, rightmost_ind]

    def _binary_search(self, nums, target, left):
        low, high = 0, len(nums)

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > target or (left and nums[mid] == target):
                high = mid
            else:
                low = mid + 1
        return low