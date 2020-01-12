from collections import defaultdict


class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return 0

        mapping = defaultdict(set)
        result = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                mapping[nums[i] + nums[j]].add((i, j))

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                two_sum = target - (nums[i] + nums[j])
                if two_sum in mapping:
                    for k, n in mapping[two_sum]:
                        if k != i and k != j and n != i and n != j:
                            result.add(tuple(sorted([nums[i], nums[j], nums[k], nums[n]])))

        return list(result)


if __name__ == "__main__":
    s = Solution()
    print(s.fourSum([-4,-3,-2,-1,0,0,1,2,3,4], 5))