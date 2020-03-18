class Solution:
    def updateMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return matrix

        dp = [[float('+inf') for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if 0 <= i - 1 < len(matrix):
                        dp[i][j] = min(dp[i][j], 1 + dp[i - 1][j])
                    if 0 <= j - 1 < len(matrix[0]):
                        dp[i][j] = min(dp[i][j], 1 + dp[i][j - 1])

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if 0 <= i + 1 < len(matrix):
                        dp[i][j] = min(dp[i][j], 1 + dp[i + 1][j])
                    if 0 <= j + 1 < len(matrix[0]):
                        dp[i][j] = min(dp[i][j], 1 + dp[i][j + 1])

        return dp