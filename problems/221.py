class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1]))

        max_square = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                max_square = max(max_square, dp[i][j])

        return max_square ** 2