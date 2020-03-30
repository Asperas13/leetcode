from math import sqrt


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        s = sorted([p1, p2, p3, p4], key=lambda a: (a[0], a[1]))
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                return False

        p1, p2, p3, p4 = s
        d1 = sqrt((p4[1] - p1[1]) ** 2 + (p4[0] - p1[0]) ** 2)
        d2 = sqrt((p3[1] - p2[1]) ** 2 + (p3[0] - p2[0]) ** 2)
        a = sqrt((p4[1] - p2[1]) ** 2 + (p4[0] - p2[0]) ** 2)
        b = sqrt((p4[1] - p3[1]) ** 2 + (p4[0] - p3[0]) ** 2)
        return d1 == d2 and a == b
