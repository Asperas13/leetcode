class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minimum_possible = float("+inf")
        cur_sum = 0
        for num in nums:
            cur_sum += num
            minimum_possible = min(cur_sum, minimum_possible)

        if minimum_possible > 0:
            return 1
        else:
            return abs(minimum_possible) + 1