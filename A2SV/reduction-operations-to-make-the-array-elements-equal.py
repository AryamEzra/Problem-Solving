class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        #time: O(n)
        #space: O(n)
        
        ans = []
        nums.sort(reverse = True)
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                ans.append(j+1)
            elif nums[j] == nums[j+1]:
                continue
        
        return sum(ans)
        
        