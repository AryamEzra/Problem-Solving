class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        #time: O(n)
        #space: O(1)
        
        ans = 0
        nums.sort(reverse = True)
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                ans += j+1
            elif nums[j] == nums[j+1]:
                continue
        
        return ans
        
        