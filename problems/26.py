class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)
        last_uniq_ind = 0
        ind_to_swap_with = 1
        cur = 1
        while cur < len(nums):
            if nums[cur] != nums[last_uniq_ind]:
                self._swap(nums, cur, ind_to_swap_with)
                last_uniq_ind = ind_to_swap_with
                ind_to_swap_with += 1
            cur += 1

        return last_uniq_ind + 1

    def _swap(self, lst, ind, ind2):
        lst[ind], lst[ind2] = lst[ind2], lst[ind]