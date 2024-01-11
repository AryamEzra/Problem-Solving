class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #time:O(n)
        #space: O(1)

        min_length = float('inf')
        start = 0
        end = 0
        cur_sum = 0
        
        while end < len(nums):
            cur_sum += nums[end]
            end += 1
            while cur_sum >= target:
                min_length = min(min_length, end - start)
                cur_sum -= nums[start]
                start += 1
                
        return min_length if min_length != float('inf') else 0
    