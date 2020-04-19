from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        threshold_x, threshold_y = abs(x), abs(y)
        directions = [(1, 2), (-1, 2), (-2, 1), (2, 1), (-2, -1), (2, -1), (-1, -2), (1, -2)]
        queue = deque()
        queue.append((threshold_x, threshold_y, 0))
        memo = {}
        while queue:
            x, y, step = queue.popleft()
            if x == 0 and y == 0:
                return step

            for xi, yi in directions:
                dx, dy = x + xi, y + yi
                if dx > -4 and dx < threshold_x + 10 and dy > -4 and dy < threshold_y + 10 and (dx, dy) not in memo:
                    memo[(dx, dy)] = True
                    queue.append((dx, dy, step + 1))

        return float("+inf")