class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = [[0 for _ in range(m)] for _ in range(n)]

        for x, y in indices:
            for j in range(n):
                matrix[j][y] += 1

            for j in range(m):
                matrix[x][j] += 1

        odd_values = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] & 1 == 1:
                    odd_values += 1

        return odd_values

