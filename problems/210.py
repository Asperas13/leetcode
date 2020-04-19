from collections import deque, defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses

        queue = deque()
        graph = defaultdict(list)
        topological_order = []
        # 0, 0, 0 2

        # [0 : [1, 2], 1 : [3], 2: [3]]
        for course, prerequisite in prerequisites:
            in_degree[course] += 1
            graph[prerequisite].append(course)

        for i, degree in enumerate(in_degree):
            if degree == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()

            topological_order.append(course)

            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        if len(topological_order) != numCourses:
            return []

        return topological_order