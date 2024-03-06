class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # you can use bisect_right or bisect_left

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                return mid
        return l
        