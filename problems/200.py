class UnionFind:
    def __init__(self, components, capacity):
        self.uf = [i for i in range(capacity)]
        self.rank = [1 for _ in range(capacity)]
        self.count = components

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)

        if i == j:
            return

        if self.rank[i] < self.rank[j]:
            self.uf[i] = j
        elif self.rank[i] > self.rank[j]:
            self.uf[j] = i
        else:
            self.uf[j] = i
            self.rank[i] += 1
        self.count -= 1

    def connected(self, i, j):
        return self.find(i) == self.find(j)

    def find(self, i):
        while self.uf[i] != i:
            i = self.uf[self.uf[i]]
        return i


class Solution:
    def numIslands(self, grid):
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        if not n:
            return 0

        components = len([1 for i in range(m) for j in range(n) if grid[i][j] == '1'])
        uf = UnionFind(components, m * n)

        def _inside(i, j):
            if 0 <= i < m and 0 <= j < n:
                return True
            return False

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    if _inside(i - 1, j) and grid[i - 1][j] == '1':
                        uf.union((i - 1) * n + j, i * n + j)
                    if _inside(i, j - 1) and grid[i][j - 1] == '1':
                        uf.union(i * n + (j - 1), i * n + j)
                    if _inside(i + 1, j) and grid[i + 1][j] == '1':
                        uf.union((i + 1) * n + j, i * n + j)
                    if _inside(i, j + 1) and grid[i][j + 1] == '1':
                        uf.union(i * n + (j + 1), i * n + j)

        return uf.count