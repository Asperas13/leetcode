class Solution:
    def subarraySum(self, nums, k: int) -> int:
        sum_mapping = Counter({0: 1})
        _sum = 0
        subarray_count = 0
        for i in range(len(nums)):
            _sum += nums[i]
            if _sum - k in sum_mapping:
                subarray_count += sum_mapping[_sum - k]

            sum_mapping[_sum] += 1

        return subarray_count