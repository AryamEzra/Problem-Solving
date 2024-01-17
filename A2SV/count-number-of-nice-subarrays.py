class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #time: O(n)
        #space: O(1)

        l = 0
        r = 0
        n = len(nums)
        ans = 0
        count = 0
        odd  = 0

        while r < n:
            if nums[r] % 2 != 0:
                odd += 1
                count = 0
            while odd == k:
                count += 1
                odd -= (nums[l] % 2 != 0)
                l += 1
            ans += count
            r += 1
        return ans
    


