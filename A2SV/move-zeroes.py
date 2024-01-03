class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #time: O(n)
        #space: O(1)

        pl = 0
        s = 0
        n = len(nums)
        while s < n:
            if nums[s] != 0:
                nums[s], nums[pl] = nums[pl], nums[s]
                pl += 1
            s += 1

        