class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0

        nums = set(nums)
        longest_subsequence = 0
        local_subsequence = 0

        while nums:
            num = nums.pop()
            nums.add(num)

            hi = num
            lo = num - 1

            while hi in nums:
                local_subsequence += 1
                nums.remove(hi)
                hi += 1

            while lo in nums:
                local_subsequence += 1
                nums.remove(lo)
                lo -= 1

            longest_subsequence = max(longest_subsequence, local_subsequence)
            local_subsequence = 0

        return longest_subsequence
