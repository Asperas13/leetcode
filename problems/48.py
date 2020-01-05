class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        i = 0
        dim = len(matrix)
        while i < dim:
            offset = 0
            while i + offset < dim:
                matrix[i + offset][i], matrix[i][i + offset] = matrix[i][i + offset], matrix[i + offset][i]
                offset += 1
            i += 1
        for j in range(dim):
            self.reverse(matrix[j])

    def reverse(self, lst):
            i, j = 0, len(lst) - 1
            while i < j:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1

            return lst