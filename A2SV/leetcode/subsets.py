class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(i, combo):
            if combo not in ans:
                ans.append(combo[:])
            if i >= n:
                return 
            backtrack(i+1, combo)
            combo.append(nums[i])
            backtrack(i+1, combo)
            combo.pop()
        backtrack(0, [])
        return ans
