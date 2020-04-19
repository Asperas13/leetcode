class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_subarray_ln = 0
        counter = {}
        counter[0] = -1
        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in counter:
                max_subarray_ln = max(max_subarray_ln, i - counter[count])
            else:
                counter[count] = i
        return max_subarray_ln