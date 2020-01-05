from collections import defaultdict


class Solution:
    def criticalConnections(self, n, connections):
        graph = defaultdict(list)

        n = len(connections)

        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)

        visited = [False]*n
        disc = [float('inf')]*n
        low = [float('inf')]*n
        parent = [-1]*n
        time = 0

        result = []

        for i in range(n):
            if visited[i] is False:
                self.get(i, graph, visited, disc, low, parent, time, result)

        return result

    def get(self, u, graph, visited, disc, low, parent, time, result):

        visited[u] = True
        disc[u] = time
        low[u] = time
        time += 1

        for v in graph[u]:
            if visited[v] is not True:
                parent[v] = u

                self.get(v, graph, visited, disc, low, parent, time, result)

                low[u] = min(low[u], low[v])

                if low[v] > disc[u]:
                    result.append([u, v])

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])
