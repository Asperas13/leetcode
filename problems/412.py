class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ['FizzBuzz' if i % 3 == 0 and i % 5 == 0 and i >= 5 else "Buzz" if i % 5 == 0 and i >= 5 else "Fizz" if i % 3 == 0 and i >= 3 else str(i) for i in range(1, n + 1)]