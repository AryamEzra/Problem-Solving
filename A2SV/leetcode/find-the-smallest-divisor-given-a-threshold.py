class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        def minimum_integer(mid):
            count = 0
            for i in range(n):
                count += ceil(nums[i] / mid)
            if count > threshold:
                return False
            return True
        l = 1
        r = sum(nums)
        while l <= r: 
            mid = (l + r) // 2
            if minimum_integer(mid): # return True
                r = mid - 1
            else:
                l = mid + 1
            
        return l