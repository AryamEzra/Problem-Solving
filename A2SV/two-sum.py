class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {}
        for i in range(len(nums)):
            curr = nums[i]
            ans = target - curr
            if ans in two_sum:
                return[two_sum[ans], i]
            two_sum[curr] = i

        