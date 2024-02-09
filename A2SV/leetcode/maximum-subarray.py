class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = 0
        cur_max = 0
        for num in nums:
            cur_max += num 
            if cur_max < 0:
                cur_max = 0
            elif cur_max > max_sum:
                max_sum = cur_max
        
        return max_sum if max_sum > 0 else max(nums)