class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        original_length = len(arr)
        i, j = 0, len(arr) - 1
        zeros_to_double = set()
        while i < j:
            if arr[i] == 0:
                zeros_to_double.add(i)
                j -= 1
            i += 1

        for i in range(len(zeros_to_double)):
            arr.append(0)

        zeros = len(zeros_to_double)
        for i in range(len(arr) - zeros - 1, -1, -1):
            if i in zeros_to_double:
                zeros_to_double.remove(i)
                arr[i + len(zeros_to_double)], arr[i + len(zeros_to_double) + 1] = 0, 0
            else:
                arr[i + len(zeros_to_double)] = arr[i]

        while len(arr) > original_length:
            arr.pop()