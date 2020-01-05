class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            self.sortColors(left)
            self.sortColors(right)

            i, j, k = 0, 0, 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1

                k += 1

            while i < len(left):
                nums[k] = left[i]
                i = i + 1
                k = k + 1

            while j < len(right):
                nums[k] = right[j]
                j = j + 1
                k = k + 1