class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        prime_number_of_set_bits = 0
        for i in range(L, R + 1):
            k = i
            count = 0
            while k != 0:
                k = k & (k - 1)
                count += 1
            if count in primes:
                prime_number_of_set_bits += 1

        return prime_number_of_set_bits
