class Solution:
    def combinationSum3(self, k, n):
        def _helper(k, n, subset, subsets, max_n):
            if len(subset) == k:
                return

            for i in range(min(max_n, 9), 0, -1):
                new_target = n - i
                if new_target < 0:
                    continue
                elif new_target == 0 and len(subset) + 1 == k:
                    s = subset.copy()
                    s.append(i)
                    subsets.append(s)
                else:
                    s = subset.copy()
                    s.append(i)
                    _helper(k, n - i, s, subsets, i - 1)
        subsets = []
        _helper(k, n, [], subsets, n)
        return subsets