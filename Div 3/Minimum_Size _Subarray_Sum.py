class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        output = float('inf')
        curr_sum = 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                output = min(output,r-l+1)
                curr_sum -= nums[l]
                l += 1
        return output if output != float('inf') else 0