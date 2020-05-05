# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first_bad_version = n
        lo, hi = 1, n
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if isBadVersion(mid) is True:
                first_bad_version = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return first_bad_version