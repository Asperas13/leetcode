from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        directions = defaultdict(set)
        endword_transformations = set()
        wordList.append(beginWord)

        if endWord not in wordList:
            return 0

        for i in range(len(endWord)):
            endword_transformations.add(endWord[:i] + '*' + endWord[i + 1:])

        for word in wordList:
            for i in range(len(word)):
                directions[word[:i] + '*' + word[i + 1:]].add(word)

        visited = {}
        min_steps = float('+inf')
        queue = deque()

        for i in range(len(beginWord)):
            queue.append((beginWord[:i] + '*' + beginWord[i + 1:], 1))

        while queue:
            transformation, steps = queue.popleft()

            if transformation in endword_transformations:
                min_steps = min(min_steps, steps + 1)

            if transformation in visited:
                continue

            visited[transformation] = 1

            for word in directions[transformation]:
                for i in range(len(word)):
                    tr = word[:i] + '*' + word[i + 1:]
                    if tr not in visited:
                        queue.append((tr, steps + 1))

        return min_steps if min_steps < float('+inf') else 0