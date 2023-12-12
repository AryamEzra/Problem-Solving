class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = sum(nums)
        ans = []
        for i in range(len(nums)):
                if nums[i] % 2 != 0:
                    total -= nums[i]
        for val, place in queries:
            tmp = nums[place]
            nums[place] += val
        
            if nums[place] % 2 == 0 and tmp % 2 == 0:
                total += val
            elif nums[place] % 2 == 0:
                total += nums[place]
            elif nums[place] % 2 == 1 and tmp % 2 == 0:
                total -= tmp
            ans.append(total)
        return ans
            



