class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #time: O(n)
        #space: O(n)

        count = 0
        cur  = 0
        dic = {0:1}
        for i in range(len(nums)):
            
            cur += nums[i]
            if cur - k in dic.keys():
                count += dic[cur-k]
            
            dic[cur] = dic.get(cur, 0) + 1
        
        return count

        