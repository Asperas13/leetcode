class Solution:
    def removeElement(self, nums, val):
        cur = 0
        while cur < len(nums):
            if nums[cur] != val:
                cur += 1
                continue
            last = len(nums) - 1
            nums[cur], nums[last] = nums[last], nums[cur]
            nums.pop(last)
        return len(nums)