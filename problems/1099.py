class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        ans = 0
        i, j = 0, len(A) - 1
        while i < j:
            if ans < A[i] + A[j] < K:
                ans = A[i] + A[j]
                i += 1
            elif A[i] + A[j] > K:
                j -= 1
            else:
                i += 1
        return ans if ans > 0 else -1
