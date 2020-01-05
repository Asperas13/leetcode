class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        return sum(map(min, [(nums[i], nums[i - 1]) for i in range(1, len(nums), 2)]))
