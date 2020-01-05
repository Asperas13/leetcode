class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0

        water = 0
        lo, hi = 0, 1
        while hi < len(height):
            upper_bound = height[lo]
            lower_bound = 0
            next_height = height[hi]
            while height[hi] < height[lo]:
                if upper_bound > height[hi] > lower_bound:
                    next_height = height[hi]
                    lower_bound = height[hi]

                hi += 1
                if hi == len(height):
                    height[lo] = next_height
                    hi = lo + 1
                    continue

            mid = lo
            while mid < hi:
                water += height[lo] - height[mid]
                mid += 1

            lo = hi
            hi += 1
        return water