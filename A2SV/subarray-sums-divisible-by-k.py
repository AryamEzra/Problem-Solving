class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #time: O(n)
        #space: O(n)

        count = 0
        cur  = 0
        dic = {0:1}
        for i in range(len(nums)):
            
            cur += nums[i]
            rem = cur % k
            if rem in dic.keys():
                count += dic[rem]
            
            dic[rem] = dic.get(rem, 0) + 1
        
        return count