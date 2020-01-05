from functools import lru_cache


class Solution:
    @lru_cache(maxsize=128)
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        for j in range(len(s3)):

            if s1 and s2 and s1[0] == s3[j] and s2[0] == s3[j]:

                return self.isInterleave(s1[1:], s2, s3[j+1:]) or self.isInterleave(s1, s2[1:], s3[j+1:])

            elif s1 and s1[0] == s3[j]:
                s1 = s1[1:]
                continue

            elif s2 and s2[0] == s3[j]:
                s2 = s2[1:]
                continue

            else:
                return False

        return True if s1 == '' and s2 == '' else False