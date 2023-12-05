class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_count = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur_count += 1
            else:
                cur_count = 0
            max_count = max(cur_count, max_count)
        return max_count

        