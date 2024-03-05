class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        cur = 0
        def backtrack(i, combo):
            nonlocal cur #to call a global varribale inside a funciton 
            if cur == target:
                ans.append(combo[:])
                return
            if i >= n:
                return
            if cur > target:
                return
                
            cur += candidates[i]
            combo.append(candidates[i])
            
            backtrack(i, combo)
            cur -= candidates[i]
            combo.pop()
            
            backtrack(i+1, combo)
        backtrack(0, [])
        return ans

        