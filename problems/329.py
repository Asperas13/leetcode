from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0

        N, M = len(matrix), len(matrix[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def _inner(y, x):
            nonlocal N, M
            return 0 <= y < N and 0 <= x < M

        @lru_cache(maxsize=None)
        def _recurse(y, x):
            max_path = 1
            for dy, dx in directions:
                if _inner(y + dy, x + dx) and matrix[y + dy][x + dx] > matrix[y][x]:
                    max_path = max(max_path, 1 + _recurse(y + dy, x + dx))

            return max_path

        max_path = float('-inf')
        for i in range(N):
            for j in range(M):
                max_path = max(max_path, _recurse(i, j))

        return max_path

