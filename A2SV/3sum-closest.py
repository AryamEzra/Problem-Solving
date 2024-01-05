class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #time: O(nlogn)
        #space: O(1)
        nums.sort()
        check = float('inf')
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return total
                if abs(total - target) < abs(check - target):
                    check = total
                if total < target:
                    left += 1
                else:
                    right -= 1
        return check

                    