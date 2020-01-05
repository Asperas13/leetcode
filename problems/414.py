class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) < 3:
            return max(nums)

        nums = list(set(nums))
        nums.sort(reverse=True)

        if len(nums) < 3:
            return max(nums)

        return nums[2]
