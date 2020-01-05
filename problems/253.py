"""
[0, 5, 15]
[10, 20, 30]
"""

"""
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        min_required = 1
        overlapping = 1

        for ind1, i1 in enumerate(intervals):
            for ind2, i2 in enumerate(intervals):
                if ind1 == ind2:
                    continue
                else:
                    if i2[0] <= i1[0] < i2[1]:
                        overlapping += 1

            min_required = max(min_required, overlapping)
            overlapping = 1

        return min_required
"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)
        c = len(intervals)
        s, e = 0, 0
        min_required = 0
        overlapping = 0
        while s < c:
            if starts[s] < ends[e]:
                s += 1
                overlapping += 1
                min_required = max(overlapping, min_required)
            else:
                e += 1
                overlapping -= 1

        return min_required