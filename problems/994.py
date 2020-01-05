class Solution:
    def orangesRotting(self, grid) -> int:
        queue = []
        visited = {}
        last_minute = 0

        def _inside(y, x):
            if 0 <= y < len(grid) and 0 <= x < len(grid[0]):
                return True
            return False

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    queue.append((y, x, 0))
                    visited[(y, x)] = True

        while queue:
            y, x, minute = queue.pop(0)
            for dy, dx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if _inside(dy, dx) and (dy, dx) not in visited and grid[dy][dx] != 0:
                    if minute + 1 > last_minute:
                        last_minute = minute + 1
                    queue.append((dy, dx, minute + 1))
                    visited[(dy, dx)] = True
                    grid[dy][dx] = 2

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return last_minute