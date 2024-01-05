class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #time: O(n**2)
        #space: O(n)
        
        ans = set()
        nums.sort()
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    x = (nums[i], nums[left], nums[right])
                    ans.add(x)
                if total <= 0:
                    left += 1
                else:
                    right -= 1

        return list(ans)

        