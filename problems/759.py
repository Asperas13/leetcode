"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        if len(schedule) < 2:
            return []

        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append(interval)

        starts = [i.start for i in sorted(intervals, key=lambda interval: interval.start)]
        ends = [i.end for i in sorted(intervals, key=lambda interval: interval.end)]

        i, j = 1, 0
        result = []
        while i < len(ends):
            if starts[i] > ends[j]:
                result.append(Interval(ends[j], starts[i]))

            i += 1
            j += 1

        return result
