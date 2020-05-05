class Solution:
    def findComplement(self, num: int) -> int:
        binary_complement = []
        while num > 0:
            binary_complement.append(not (num % 2))
            num //= 2

        complement = 0
        rank = 0

        for i in range(len(binary_complement)):
            if binary_complement[i]:
                complement += pow(2, rank)
            rank += 1

        return complement