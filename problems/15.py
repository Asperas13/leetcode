class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        result = []
        nums.sort()
        combinations = {}
        num_to_ind = {v: i for i, v in enumerate(nums)}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                k_num = -(nums[i] + nums[j])
                k = num_to_ind.get(k_num, -1)
                if k > j and (nums[i], nums[j], k_num) not in combinations:
                    combinations[(nums[i], nums[j], k_num)] = 1
                    result.append((nums[i], nums[j], k_num))

        return result
