class Solution:
    def plusOne(self, digits):
        if not digits:
            return [1]

        num_to_add = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + num_to_add

            if digits[i] == 10:
                digits[i] = 0
                num_to_add = 1
            else:
                num_to_add = 0
                break

        if num_to_add == 1:
            digits.insert(0, 1)

        return digits

if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([2,2,2]))
    print(s.plusOne([]))
    print(s.plusOne([9]))
    print(s.plusOne([2,9,9,9]))
    print(s.plusOne([9,9,9,9]))