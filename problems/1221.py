class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L, R = 0, 0
        splits = 0

        for ch in s:
            if ch == 'R':
                R += 1
            else:
                L += 1

            if L == R and L != 0:
                L, R = 0, 0
                splits += 1

        return splits