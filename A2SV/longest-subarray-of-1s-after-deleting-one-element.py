class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #time: O(n)
        #space: O(1)

        zero_count = 0
        left = 0
        right = 0
        longest = 0
        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            right += 1
            longest = max(longest, right - left - 1)
        return longest


                
        