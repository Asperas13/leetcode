class Solution:
    def findMin(self, nums) -> int:
        if not nums:
            return -1
        elif len(nums) == 1:
            return nums[0]

        lo, hi = 0, len(nums) - 1

        if nums[lo] < nums[hi]:
            return nums[lo]

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[lo]:
                lo = mid + 1
            else:
                hi = mid - 1

        return nums[0]
