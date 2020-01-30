from collections import Counter


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        letters = Counter(S)
        result = []
        current_partition = set()
        partition_size = 0

        for letter in S:
            current_partition.add(letter)
            letters[letter] -= 1
            partition_size += 1

            if letters[letter] == 0:
                current_partition.remove(letter)

            if not current_partition:
                result.append(partition_size)
                partition_size = 0

        return result
