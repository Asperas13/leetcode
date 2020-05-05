class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort(key=lambda a: a[0])
        i, j = 0, 0
        answer = [0] * len(nums)
        while i < len(nums):
            while j < len(nums) and nums[j][0] == nums[i][0]:
                answer[nums[j][1]] = i
                j += 1
            i = j

        return answer

