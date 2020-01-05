class Solution:
    def combinationSum(self, candidates, target):
        def _helper(array, target, subset, cur_sum, subsets, from_ind):
            for i in range(from_ind, -1, -1):
                new_cur_sum = cur_sum + array[i]
                if new_cur_sum > target:
                    continue
                elif new_cur_sum == target:
                    s = subset.copy()
                    s.append(array[i])
                    subsets.append(s)
                else:
                    s = subset.copy()
                    s.append(array[i])
                    _helper(array, target, s, new_cur_sum, subsets, i)
        subsets = []
        _helper(candidates, target, [], 0, subsets, len(candidates) - 1)
        return subsets