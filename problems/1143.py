class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        common_letters = set(text1) | set(text2)

        text1 = ''.join([ch for ch in text1 if ch in common_letters])  # ace
        text2 = ''.join([ch for ch in text2 if ch in common_letters])  # ace
        if not text1 or not text2:
            return 0

        dp = [[0 for _ in range(len(text1) + 1)] for _ in range(len(text2) + 1)]

        for i in range(len(text1) + 1):
            dp[0][i] = 0

        for i in range(len(text2) + 1):
            dp[i][0] = 0

        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text2[i - 1] == text1[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

        return dp[len(text2)][len(text1)]