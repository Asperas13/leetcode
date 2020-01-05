from functools import lru_cache

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        l, r = 0, arrLen - 1

        @lru_cache(maxsize=None)
        def _helper(steps_remains, cur_index):
            if cur_index < l or cur_index > r:
                return 0
            if steps_remains == 0:
                if cur_index == 0:
                    return 1
                return 0
            if cur_index == steps_remains:
                return 1
            if cur_index > steps_remains:
                return 0

            return _helper(steps_remains - 1, cur_index) + _helper(steps_remains - 1, cur_index + 1) + _helper(steps_remains - 1, cur_index - 1)

        _helper(steps, 0)
        return _helper(steps, 0) % 1000000007