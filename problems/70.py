class Solution:
    def climbStairs(self, n):
        s = [0 for _ in range(n + 1)]
        s[0], s[1] = 1, 1
        for i in range(2, n + 1):
            s[i] = s[i - 1] + s[i - 2]
        return s[n]