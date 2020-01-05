class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for _ in range(len(nums))]
        total_multiplying = 1
        zero_count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                total_multiplying *= nums[i]

        if zero_count > 1:
            return [0 for _ in range(len(nums))]
        else:
            for i in range(len(output)):
                if nums[i] == 0:
                    output[i] = total_multiplying
                elif nums[i] != 0 and zero_count:
                    output[i] = 0
                else:
                    output[i] = int(total_multiplying / nums[i])

        return outputw