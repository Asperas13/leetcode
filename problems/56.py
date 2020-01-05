class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda a: a[0])
        prev = intervals[0]
        result = []
        for i in range(1, len(intervals)):
            if intervals[i][0] >= prev[0] and intervals[i][0] <= prev[1]:
                prev[0] = min(prev[0], intervals[i][0])
                prev[1] = max(prev[1], intervals[i][1])
            else:
                result.append(prev)
                prev = intervals[i]

        result.append(prev)
        return result