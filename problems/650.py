class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """

        return int(sum(self.primfacs(n)))

    def primfacs(self, n):
        i = 2
        primfac = []
        while i * i <= n:
            while n % i == 0:
                primfac.append(i)
                n = n / i
            i = i + 1
        if n > 1:
            primfac.append(n)
        return primfac