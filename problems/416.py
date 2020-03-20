from functools import lru_cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum & 1 == 1:
            return False

        @lru_cache(maxsize=None)
        def _partition(first_sum, cur_index):
            nonlocal total_sum
            if first_sum == total_sum - first_sum:
                return True
            if cur_index == len(nums) or first_sum > total_sum - first_sum:
                return False

            return _partition(first_sum + nums[cur_index], cur_index + 1) or _partition(first_sum, cur_index + 1)

        return _partition(0, 0)