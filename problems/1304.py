class Solution:
    def sumZero(self, n: int) -> List[int]:
        zero_sum_array = []
        if n & 1 == 1:
            zero_sum_array.append(0)
            n -= 1

        c = 1
        while n > 0:
            zero_sum_array.append(c)
            zero_sum_array.append(-c)
            n -= 2
            c += 1

        return zero_sum_array