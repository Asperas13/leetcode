# DP
"""
class Solution:
    def canJump(self, nums):
        can_reach = [False] * len(nums)
        can_reach[len(nums) - 1] = True
        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, min(len(nums), nums[i] + 1)):
                can_reach[i] = can_reach[i + j]
                if can_reach[i]:
                    break
        return can_reach[0]
"""


class Solution:
    def canJump(self, nums):
        closest_answer = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i < closest_answer <= i + nums[i]:
                closest_answer = i

        return closest_answer == 0