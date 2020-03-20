from functools import lru_cache


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.dp = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            cur_sum = 0
            for j in range(len(matrix[i])):
                cur_sum += matrix[i][j]
                self.dp[i][j] = cur_sum

    @lru_cache(maxsize=None)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region_sum = 0
        for i in range(row1, row2 + 1):
            if col1 == 0:
                region_sum += self.dp[i][col2]
            else:
                region_sum += self.dp[i][col2] - self.dp[i][col1 - 1]
        return region_sum

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)