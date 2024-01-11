class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        len_wind  = 0
        l = 0
        r = 0
        summ = 0
        while r < len(nums):
            summ += nums[r]
            while summ + k < nums[r] * (r - l + 1):
                
                summ -= nums[l]
                l += 1
            len_wind = max(len_wind, r-l+1)
            r += 1
    
                
        return len_wind
                


