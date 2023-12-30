class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #time: O(nlogn)
        #space: O(n)

        if all(num == 0 for num in nums):
            return "0"

        nums =  [str(num) for num in nums]
        def compare(x,y):
            return int(y+x) - int(x+y)
        nums.sort(key=cmp_to_key(compare))
        return "".join(nums)

        
        

        