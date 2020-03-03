class Solution:
    def findPeakElement(self, nums) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = lo + ((hi - lo) // 2)

            if (mid == 0 or nums[mid] > nums[mid - 1]) and (mid == len(nums) - 1 or nums[mid] > nums[mid + 1]):
                return mid
            elif nums[mid] > nums[mid - 1]:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo + 1


if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement([1,2]))