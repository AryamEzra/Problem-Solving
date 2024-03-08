class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        mod = (10 ** 9) + 7
        count = 0
        for i in range(n):
            if 2 * nums[i] <= target:
                diff = abs(target - nums[i])
                idx = bisect_right(nums, diff)
                count += 2 ** (idx - i - 1)
            
        count = floor(count)
        count %= mod
        return count
            

            

        
