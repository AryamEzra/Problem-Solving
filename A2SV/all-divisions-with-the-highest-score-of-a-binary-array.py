class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        #time: O(n)
        #space: O(n)

        zero = 0
        one = nums.count(1)
        ans = [zero+one]
        n = len(nums)
        for i in range(n+1):
            
            if i < len(nums) and nums[i] == 0:
                zero += 1
            else:
                one -= 1
            ans.append(zero+one)
        max_ans = max(ans)
        
    
        res = defaultdict(list)
        for i in range(n+1):
            res[ans[i]].append(i)
        return res[max_ans]
        
        



         