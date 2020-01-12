class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = set()

        def _update_subset(subset, i):
            if i == len(nums):
                subsets.add(tuple(sorted(subset)))
            else:
                sub = subset.copy()
                sub.append(nums[i])
                _update_subset(sub, i + 1)
                _update_subset(subset, i + 1)

        _update_subset([], 0)
        return list(subsets)