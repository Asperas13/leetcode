class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        def _binary_search(array, target):
            lo, hi = 0, len(array) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if array[mid] == target:
                    return True
                elif array[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return False

        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if n == 1:
                if matrix[i][0] == target:
                    return True
            else:
                if matrix[i][0] <= target <= matrix[i][-1]:
                    return _binary_search(matrix[i], target)
        return False