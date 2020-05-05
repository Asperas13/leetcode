class Solution:
    def firstMissingPositive(self, nums):
        min_val = float('+inf')
        max_val = float('-inf')
        actual_sum_of_positive_nums = 0
        non_positive_nums = 0
        for num in nums:
            if num < min_val and num > 0:
                min_val = num

            if num > max_val and num > 0:
                max_val = num

            if num <= 0:
                non_positive_nums += 1
            else:
                actual_sum_of_positive_nums += num

        sum_of_positive_nums = (min_val + max_val) / 2 * (max_val + 1 - min_val)

        if min_val > 1:
            return 1
        elif sum_of_positive_nums != actual_sum_of_positive_nums:
            return int(sum_of_positive_nums - actual_sum_of_positive_nums)
        else:
            return int(max_val + 1)
