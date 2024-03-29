from collections import deque


class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        """
        self.available_numbers = deque()
        for i in range(maxNumbers):
            self.available_numbers.append(i)
        self.assigned_numbers = {}

    def get(self) -> int:
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        """
        if not self.available_numbers:
            return -1
        number = self.available_numbers.popleft()
        self.assigned_numbers[number] = number
        return number

    def check(self, number: int) -> bool:
        """
        Check if a number is available or not.
        """
        if number in self.assigned_numbers:
            return False
        return True

    def release(self, number: int) -> None:
        """
        Recycle or release a number.
        """
        if number in self.assigned_numbers:
            del self.assigned_numbers[number]
            self.available_numbers.append(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)