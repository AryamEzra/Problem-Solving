class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        ans1 = -1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                ans1 = mid
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        l = 0
        r = len(nums) - 1
        ans2 = -1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target:
                ans2 = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return [ans1, ans2]


        