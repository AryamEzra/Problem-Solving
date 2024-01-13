class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        cur_len = 0
        l = 0
        r = 0
        max_len = 0
        n = len(nums)
        zero_count = 0
        while r < n:
            if nums[r] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1

            cur_len = r - l + 1
            max_len = max(max_len, cur_len)
            r += 1
        return max_len