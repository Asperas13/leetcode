class Comparator(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ''

        for i in range(len(nums)):
            nums[i] = str(nums[i])

        nums.sort(key=Comparator)

        if nums[0].startswith("0"):
            return "0"

        return "".join(nums)