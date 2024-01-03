class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        #time: O(nlogn)
        #space: O(1)

        l = 0
        r = len(nums) - 1
        ans = 0
        nums.sort()
        while l < r:
            if nums[l] + nums[r] < target:
                ans += r - l
                l += 1
            else:
                r -= 1
        return ans
        
        