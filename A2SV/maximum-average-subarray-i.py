class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #time: O(n)
        #space: O(1)

        current_sum = sum(nums[:k])
        ans = current_sum

        for i in range(k, len(nums)):
            current_sum += (nums[i] - nums[i-k])
            ans = max(ans, current_sum)
        return ans / k




        