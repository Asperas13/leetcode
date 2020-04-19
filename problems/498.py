# (0, 1) -> (1, 0)

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        in_reverse = True
        output = []
        i, j = 0, 0
        reverse_i, reverse_j = 0, 0
        while i != len(matrix) - 1 or j != len(matrix[0]) - 1:
            if not in_reverse:
                i1, j1 = i, j
                while (i1, j1) != (reverse_i + 1, reverse_j - 1):
                    output.append(matrix[i1][j1])
                    i1 += 1
                    j1 -= 1

            else:
                i1, j1 = reverse_i, reverse_j
                while (i1, j1) != (i - 1, j + 1):
                    output.append(matrix[i1][j1])
                    i1 -= 1
                    j1 += 1

            if j == len(matrix[0]) - 1:
                i += 1
            else:
                j += 1

            if reverse_i == len(matrix) - 1:
                reverse_j += 1
            else:
                reverse_i += 1

            in_reverse = not in_reverse

        output.append(matrix[i][j])
        return output
