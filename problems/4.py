class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        N = len(nums1) + len(nums2)
        is_even = True if N & 1 == 0 else False
        merged = []
        if not N:
            return 0

        i, j = 0, 0
        while i < len(nums1) or j < len(nums2):
            if i >= len(nums1):
                merged.append(nums2[j])
                j += 1
            elif j >= len(nums2):
                merged.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        if is_even:
            return (merged[N // 2 - 1] + merged[N // 2]) / 2
        else:
            return merged[N // 2]



s = Solution()
assert s.findMedianSortedArrays([], []) == 0
assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
assert s.findMedianSortedArrays([1, 1, 1, 1, 1, 2], [3]) == 1
assert s.findMedianSortedArrays([1, 1, 1, 1, 1], []) == 1
assert s.findMedianSortedArrays([1, 3], [2]) == 2
assert s.findMedianSortedArrays([1], [2]) == 1.5
assert s.findMedianSortedArrays([1, 3, 5], [2, 4, 6]) == 3.5
assert s.findMedianSortedArrays([1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3], [2, 2, 2, 2, 2, 2]) == 2
assert s.findMedianSortedArrays([], [2, 3]) == 2.5
assert s.findMedianSortedArrays([1], [2, 3]) == 2
assert s.findMedianSortedArrays([3,4], [1,2,5,6]) == 3.5
assert s.findMedianSortedArrays([], [1, 2, 3, 4]) == 2.5