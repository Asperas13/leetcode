class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []

        s = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                s = i - 1
                k = i
                for j in range(i, len(nums)):
                    if nums[j] <= nums[k] and nums[j] > nums[s]:
                        k = j

                nums[s], nums[k] = nums[k], nums[s]
                break

        i, j = s + 1, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1