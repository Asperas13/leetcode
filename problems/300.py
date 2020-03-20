class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [None for _ in range(len(nums))]
        for j in range(len(nums) - 1, -1, -1):
            greater_elements = 1
            for i in range(j, len(nums)):
                if nums[i] > nums[j]:
                    greater_elements = max(greater_elements, 1 + dp[i])
            dp[j] = greater_elements

        return max(dp)