class Solution:
    def searchInsert(self, nums, target):
        low, mid, high = 0, 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if mid == 0 and nums[mid] > target:
                return 0
            elif mid == len(nums) - 1 and nums[mid] < target:
                return len(nums)
            elif nums[mid - 1] < target <= nums[mid]:
                return mid
            elif nums[mid - 1] <= target < nums[mid]:
                return mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return mid