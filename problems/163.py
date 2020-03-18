class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ranges = []

        if not nums:
            if lower == upper:
                ranges.append(str(lower))
            else:
                ranges.append('%s->%s' % (lower, upper))
            return ranges

        if lower < nums[0]:
            if lower == nums[0] - 1:
                ranges.append(str(nums[0] - 1))
            else:
                ranges.append('%s->%s' % (lower, nums[0] - 1))

        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i - 1]) > 1:
                if abs(nums[i] - nums[i - 1]) == 2:
                    ranges.append(str(nums[i] - 1))
                else:
                    ranges.append('%s->%s' % (nums[i - 1] + 1, nums[i] - 1))

        if nums[len(nums) - 1] < upper:
            if nums[len(nums) - 1] + 1 == upper:
                ranges.append(str(nums[len(nums) - 1] + 1))
            else:
                ranges.append('%s->%s' % (nums[len(nums) - 1] + 1, upper))

        return ranges