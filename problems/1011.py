class Solution:
    def shipWithinDays(self, weights, D) -> int:
        lo, hi = max(weights), sum(weights)
        min_capacity = float('+inf')
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)

            days, capacity = 1, 0
            for i in range(len(weights)):
                if capacity + weights[i] > mid:
                    capacity = 0
                    days += 1
                capacity += weights[i]

            if days <= D:
                min_capacity = min(min_capacity, mid)
                hi = mid - 1
            else:
                lo = mid + 1

        return min_capacity