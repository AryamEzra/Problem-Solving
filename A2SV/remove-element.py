class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #time: O(n)
        #space: O(1)

        pl = 0
        seek = 0
        n = len(nums)
        count = n
        
        while seek < n:
            if nums[seek] != val:
                nums[seek], nums[pl] = nums[pl] , nums[seek]
                pl += 1
            seek += 1
        
        for i in range(n):
            if nums[i] == val:
                nums[i] = "_"
                count -= 1
        return count
        return nums
            
        