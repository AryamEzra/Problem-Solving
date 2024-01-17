class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        #time: O(n)
        #space: O(n)

        ans = 0
        res = []
        for i in range(len(nums)):
            ans += nums[i]
            res.append(ans)
        return res