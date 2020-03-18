class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return False

        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[lo]:
                if target >= nums[lo] and target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[mid] < nums[lo]:
                if target > nums[mid] and target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                lo += 1
        return False