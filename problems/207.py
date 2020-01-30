from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        todo = {i: set() for i in range(numCourses)}
        graph = defaultdict(set)

        for from_course, to_course in prerequisites:
            todo[from_course].add(to_course)
            graph[to_course].add(from_course)

        queue = deque([])
        for from_course, to_course in todo.items():
            if len(to_course) == 0:
                queue.append(from_course)

        while queue:
            node = queue.popleft()
            for from_course in graph[node]:
                todo[from_course].remove(node)
                if len(todo[from_course]) == 0:
                    queue.append(from_course)
            todo.pop(node)

        return not todo