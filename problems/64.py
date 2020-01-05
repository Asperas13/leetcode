class Solution:
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])

        if n == 1 and m == 1:
            return grid[0][0]

        min_sums = {}

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i == 1 and j == 1:
                    min_sums[(i, j)] = grid[i - 1][j - 1]
                elif i == 1:
                    min_sums[(i, j)] = min_sums[(i, j - 1)] + grid[i - 1][j - 1]
                elif j == 1:
                    min_sums[(i, j)] = min_sums[(i - 1), j] + grid[i - 1][j - 1]
                else:
                    min_sums[(i, j)] = min(min_sums[(i - 1, j)], min_sums[(i, j - 1)]) + grid[i - 1][j - 1]

        return min_sums[(n, m)]