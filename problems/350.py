class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        bigger = self.get_max(nums1, nums2)
        lower = self.get_min(nums1, nums2)
        res = []
        for i in lower:
            for j in bigger:
                if i == j and res.count(i) < min(lower.count(i), bigger.count(i)):
                    res.append(i)
        return res

    def get_min(self, nums1, nums2):
        return nums1 if len(nums1) <= len(nums2) else nums2

    def get_max(self, nums1, nums2):
        return nums1 if len(nums1) > len(nums2) else nums2