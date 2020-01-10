class Solution:
    def find132pattern(self, nums):
        if len(nums) < 3:
            return False

        stack = []
        min_num = min(nums)
        mins = [min_num for _ in range(len(nums))]
        mins[0] = nums[0]
        for i in range(1, len(nums)):
            mins[i] = min(mins[i - 1], nums[i])

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > mins[j]:
                while len(stack) > 0 and stack[len(stack) - 1] <= mins[j]:
                    stack.pop()
                if len(stack) > 0 and stack[len(stack) - 1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False