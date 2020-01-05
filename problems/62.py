class Solution:
    def uniquePaths(self, m, n):
        if m == 1 or n == 1:
            return 1

        paths = {}
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                paths[(i, j)] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i == 1 and j == 1:
                    paths[(i, j)] = 1
                elif i == 1:
                    paths[(i, j)] = paths[(i, j - 1)]
                elif j == 1:
                    paths[(i, j)] = paths[(i - 1, j)]
                else:
                    paths[(i, j)] = paths[(i - 1, j)] + paths[(i, j - 1)]

        return paths[(n, m)]