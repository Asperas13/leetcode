class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        dim_y = len(matrix) - 1
        dim_x = len(matrix[0]) - 1
        i, j = 0, 0
        while True:
            if matrix[i][j] >= target:
                if matrix[i][j] == target\
                        or self.binary_search([matrix[i][k] for k in range(0, j + 1)], target) is not None\
                        or self.binary_search([matrix[k][j] for k in range(0, i + 1)], target) is not None:
                    return True

            if i + 1 > dim_y and j + 1 > dim_x:
                break

            if i < dim_y:
                i += 1
            if j < dim_x:
                j += 1

        return False

    def binary_search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] == target:
                return target
            else:
                hi = mid - 1

        return None