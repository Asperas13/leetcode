from collections import defaultdict


class Solution:
    def groupStrings(self, strings):
        grouped_by_shifts = defaultdict(list)

        for string in strings:
            if len(string) <= 1:
                grouped_by_shifts['0'].append(string)
            else:
                hash_value = '0,'
                for i in range(1, len(string)):
                    hash_value += str((ord(string[i]) - ord(string[i - 1]) + 26) % 26) + ','

                grouped_by_shifts[hash_value].append(string)

        return grouped_by_shifts.values()