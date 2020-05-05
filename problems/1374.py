class Solution:
    def generateTheString(self, n: int) -> str:
        generated_string = ""
        if n & 1 == 0:
            generated_string += 'a'
            n -= 1

        if n > 0:
            generated_string += 'b' * n

        return generated_string