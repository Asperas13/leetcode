class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        pascal_triangle = []
        for i in range(1, numRows + 1):
            row = []
            if i == 1:
                pascal_triangle.append([1])
                continue

            for j in range(1, i + 1):
                if j == 1 or j == i:
                    row.append(1)
                else:
                    row.append(pascal_triangle[i - 2][j - 2] + pascal_triangle[i - 2][j - 1])

            pascal_triangle.append(row)
        return pascal_triangle
