class Solution:
    def numSmallerByFrequency(self, queries, words):
        def _binary_search(array, x):
            lo, hi = 0, len(array)

            while lo < hi:
                mid = lo + ((hi - lo) // 2)

                if array[mid] > x:
                    hi = mid
                else:
                    lo = mid + 1

            return len(array) - hi

        smallest_character_frequency = sorted([s.count(min(s)) for s in words])
        answer = []

        for q in queries:
            answer.append(_binary_search(smallest_character_frequency, q.count(min(q))))

        return answer
