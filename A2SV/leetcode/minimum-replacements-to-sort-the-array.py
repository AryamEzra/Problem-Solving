class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        sor = sorted(nums)
        if nums == sor:
            return 0
        count = 0
        cur_max = nums[-1]
        check = 0
        for i in range(len(nums)-2, -1, -1):
            cur = nums[i]
            if cur >= cur_max:
                check = ceil(cur / cur_max)
                cur_max = min(floor(cur/check), cur_max)
                count += (check - 1)
            else:
                cur_max = min(nums[i], cur_max)
        return count