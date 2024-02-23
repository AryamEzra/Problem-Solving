class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        running_sum = nums[0]
        cur_max = nums[0]
        for i in range(1, len(nums)):
            running_sum += nums[i]
            if nums[i] > cur_max:
                cur_max = max(cur_max, ceil(running_sum / (i+1)))
        return cur_max

                
        
        



            

        