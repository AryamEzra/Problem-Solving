class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cur = 1
        count = 0
        i = 0
        while cur <= n:
            if i < len(nums) and cur >= nums[i]:
                cur += nums[i]
                i += 1
            else:
                cur *= 2
                count += 1
            
        return count

        
        