class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        t = round(A.count(max(A)) / 2)

        for i in range(len(A)):
            if t == 0:
                return A.index(max(A))
            else:

                if a[i] == max(A):
                    a[i] = None
                    t -= 1

