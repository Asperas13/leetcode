class Solution:
    def countNegatives(self, grid) -> int:
        negatives = 0

        for i in range(len(grid)):
            row = grid[i]
            lo, hi = 0, len(row) - 1

            while lo <= hi:
                mid = lo + (hi - lo) // 2

                if row[mid] >= 0:
                    lo = mid + 1
                else:
                    hi = mid - 1

            if lo < len(grid[i]) and row[lo] < 0:
                negatives += len(row) - lo

        return negatives