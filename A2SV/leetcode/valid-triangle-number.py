class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        
        for c in range(len(nums)-1, -1, -1):
            r = c - 1
            l = 0
            while l < r:
                if nums[l] + nums[r] > nums[c]:
                    ans += (r-l)
                    r -= 1
                else:
                    l += 1
        return ans


        
        