class Solution:
    def combinationSum2(self, candidates, target):
        def _helper(ind_to_pick, cur_sum, cur_subset, subsets):
            if cur_sum > target:
                return
            elif cur_sum == target and cur_subset not in visited:
                subsets.append(cur_subset)
                visited.add(cur_subset)
            else:
                if ind_to_pick == len(candidates):
                    return
                new_cur_sum = cur_sum + candidates[ind_to_pick]
                _helper(ind_to_pick + 1, new_cur_sum, (*cur_subset, candidates[ind_to_pick]), subsets)
                _helper(ind_to_pick + 1, cur_sum, cur_subset, subsets)

        candidates = list(sorted(candidates))
        visited = set()
        subsets = []
        _helper(0, 0, (), subsets)
        return subsets