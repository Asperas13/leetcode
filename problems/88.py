class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1 or not nums2:
            return nums1

        for i in range(m - 1, -1, -1):
            if i == m:
                break
            nums1[i], nums1[i + n] = nums1[i + n], nums1[i]

        i, j, k = n, 0, 0
        while i < len(nums1) or j < len(nums2):
            if i == len(nums1):
                nums1[k] = nums2[j]
                j += 1
            elif j == len(nums2):
                nums1[k] = nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1

            k += 1

        return nums1


if __name__ == '__main__':
    s = Solution()
    print(s.merge([0], 0, [1], 1))