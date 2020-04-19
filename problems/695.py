class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def is_valid(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                return True

            return False

        def dfs(i, j):
            size = 1
            grid[i][j] = 0

            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if is_valid(i + di, j + dj):
                    size += dfs(i + di, j + dj)

            return size

        if len(grid) == 0 or len(grid[0]) == 0:  # [], [[]]
            return 0
        M, N = len(grid), len(grid[0])

        max_island = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    max_island = max(dfs(i, j), max_island)

        return max_island
