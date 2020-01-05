def to_bits(num):
    res = ''
    while num > 0:
        res = str(num % 2) + res
        num = num // 2

    res = '0' + res
    return res


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        bits1 = to_bits(x)
        bits2 = to_bits(y)

        len1 = len(bits1)
        len2 = len(bits2)

        if len1 > len2:
            bits2 = (len1 - len2) * '0' + bits2
        else:
            bits1 = (len2 - len1) * '0' + bits1

        res = 0

        for i in range(0, max(len1, len2)):
            if bits1[i] != bits2[i]:
                res += 1

        return res
