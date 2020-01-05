class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        max_row = [max(i) for i in grid]
        max_column = [max(i) for i in zip(*grid)]

        return sum([
            sum([min(max_row[i], max_column[j]) - grid[j][i] for i in range(len(grid[0]))]) for j in
            range(len(grid[0]))])

