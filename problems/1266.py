class Solution:
    def minTimeToVisitAllPoints(self, points):
        minutes = 0
        if len(points) < 2:
            return 0
        for i in range(1, len(points)):
            m1 = min(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1]))
            m2 = max(abs(points[i][0] - points[i - 1][0]), abs(points[i][1] - points[i - 1][1])) - m1
            minutes += m1 + m2

        return minutes