class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum of arrys - sum of the input arrays to find the remaining one
        #add the list of arrays and sybtract the reamining ones from the given list. 
        res = len(nums)
        for i in range(len(nums)):
            res += (i- nums[i])
        return res