class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()

        cur_count = 0
        max_count = 0
        if len(nums) == 0:
            max_count = 0
            return max_count
        else: 
            for i in range(len(nums)-1):
                
                    if nums[i+1] - nums[i] == 1:
                        cur_count += 1
                        max_count = max(max_count, cur_count)
                    else:
                        cur_count = 0
                    
            return max_count + 1
        