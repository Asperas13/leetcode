from collections import defaultdict


class Edge:
    def __init__(self, from_node, to_node, value):
        self.from_node = from_node
        self.to_node = to_node
        self.value = value


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for equation, value in zip(equations, values):
            a, b = equation
            graph[a][a] = Edge(a, a, 1)
            graph[b][b] = Edge(b, b, 1)
            graph[a][b] = Edge(a, b, value)
            graph[b][a] = Edge(b, a, 1 / value)

        def _dfs(from_node, to_node, current_value, graph, visited):
            if from_node in visited:
                return -1

            if graph[from_node].get(to_node):
                return graph[from_node][to_node].value * current_value

            visited[from_node] = True

            value = -1
            for node in graph[from_node]:
                value = max(value, _dfs(node, to_node, current_value * graph[from_node][node].value, graph, visited))

            return value

        response = []
        for query in queries:
            a, b, = query
            if a not in graph or b not in graph:
                response.append(-1)
            elif graph[a].get(b):
                response.append(graph[a][b].value)
            else:
                response.append(_dfs(a, b, 1, graph, {}))

        return response