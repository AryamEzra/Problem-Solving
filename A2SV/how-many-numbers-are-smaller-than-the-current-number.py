class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_list = sorted(nums)
        dic = {}
        result = []
        
        for i in range(len(nums)):
            if sorted_list[i] not in dic:
                dic[sorted_list[i]] = i
        for i in nums:
            result.append(dic[i])
        return result
        