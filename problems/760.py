class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        l = {}

        for i in range(len(B)):
            l[B[i]] = i

        return [l[i] for i in A]