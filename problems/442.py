# 36
# 25 == 36 -5 - 6
# 30

# [4, 3, 2, 7, 8, 2, 3, 1]
# [4, 3, 2, -7, 8, 2, 3, 1]
# [4, 3, -2, -7, 8, 2, 3, 1]
# [4, -3, -2, 7, 8, 2, 3, 1]
# [4, -3, -2, 7, 8, 2, -3, 1]
# [4, -3, -2, 7, 8, 2, -3, -1]

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for i in range(len(nums)):
            k = nums[i]
            if k < 0:
                k = -k
            if nums[k - 1] < 0:
                duplicates.append(k)
            else:
                nums[k - 1] = -nums[k - 1]
        return duplicates