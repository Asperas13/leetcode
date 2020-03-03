class Solution:
    """
    @param n: n nodes labeled from 0 to n - 1
    @param edges: a undirected graph
    @return:  a list of all the MHTs root labels
    """

    def findMinHeightTrees(self, n, edges):
        if n <= 2:
            return [i for i in range(n)]

        graph = self.buildGraph(n, edges)
        indegrees = self.getIndegrees(n, graph)

        queue = collections.deque(
            [node for node in indegrees if indegrees[node] == 1])

        while queue:
            res, size = list(queue), len(queue)

            for _ in range(size):
                node = queue.popleft()
                for neighbor in graph[node]:
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 1:
                        queue.append(neighbor)

        return res

    def buildGraph(self, n, edges):
        graph = {i: set() for i in range(n)}

        for node, neighbor in edges:
            graph[node].add(neighbor)
            graph[neighbor].add(node)

        return graph

    def getIndegrees(self, n, graph):
        indegrees = {i: 0 for i in range(n)}

        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1

        return indegrees
