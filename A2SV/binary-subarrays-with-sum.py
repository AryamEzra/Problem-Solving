class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        #time: O(n)
        #space: O(n)

        count = 0
        cur  = 0
        dic = {0:1}
        for i in range(len(nums)):
            
            cur += nums[i]
            if cur - goal in dic.keys():
                count += dic[cur-goal]
            
            dic[cur] = dic.get(cur, 0) + 1
        
        return count