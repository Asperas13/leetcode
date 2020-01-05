from collections import Counter


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        d = Counter()
        for i in s1:
            d[i] += 1

        parts = []

        for i in range(len(s1), len(s2) + 1, 1):
            parts.append(s2[i - len(s1):i])

        for j in parts:
            if all(j.count(i) == d.get(i, '') for i in j):
                return True

        return False