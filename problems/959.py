class UnionFind:
    def __init__(self, capacity):
        self.uf = [i for i in range(capacity)]
        self.rank = [1 for _ in range(capacity)]

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

    def connected(self, i, j):
        return self.find(i) == self.find(j)

    def find(self, i):
        while self.uf[i] != i:
            i = self.uf[self.uf[i]]
        return i


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        uf = UnionFind(N * N * 4)

        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                r = 4 * (N * i + j)
                if val in '/ ':
                    uf.union(r, r + 1)
                    uf.union(r + 2, r + 3)
                if val in '\ ':
                    uf.union(r, r + 2)
                    uf.union(r + 1, r + 3)

                if i + 1 < N: uf.union(r + 3, (r + 4 * N) + 0)
                if i - 1 >= 0: uf.union(r + 0, (r - 4 * N) + 3)
                # east/west
                if j + 1 < N: uf.union(r + 2, (r + 4) + 1)
                if j - 1 >= 0: uf.union(r + 1, (r - 4) + 2)

        return sum(uf.find(x) == x for x in range(4 * N * N))