class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if len(arr) < 2:
            return []

        arr.sort()
        min_diff = float("+inf")
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i - 1])
            min_diff = min(min_diff, diff)

        answer = []
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i - 1])
            if diff == min_diff and diff != 0:
                answer.append([min(arr[i], arr[i - 1]), max(arr[i], arr[i - 1])])

        return answer