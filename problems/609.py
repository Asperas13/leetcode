import os.path
from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        duplicates = defaultdict(list)

        for path in paths:
            directory, *files = path.split(' ')
            for _file in files:
                file_name, file_content = _file.split('(')
                file_content = file_content[:len(file_content) - 1]
                duplicates[file_content].append(os.path.join(directory, file_name))

        return [j for j in duplicates.values() if len(j) > 1]