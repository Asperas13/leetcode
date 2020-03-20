class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [None for _ in range(len(nums))]
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            self.dp[i] = cur_sum

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.dp[j]
        return self.dp[j] - self.dp[i - 1]

    # Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)