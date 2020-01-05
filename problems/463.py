class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        perimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    perimeter += 4

                    if 0 <= i - 1 < len(grid) and grid[i - 1][j] == 1:
                        perimeter -= 2

                    if 0 <= j - 1 < len(grid[0]) and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter