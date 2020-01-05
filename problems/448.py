class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(0, len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]

        res = []
        for i, num in enumerate(nums):
            if num > 0:
                res.append(i + 1)

        return res