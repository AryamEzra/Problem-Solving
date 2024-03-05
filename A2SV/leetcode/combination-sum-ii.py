class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        cur = 0

        candidates.sort()
        l = len(candidates)

        def backtrack(first_sum, combo):
            nonlocal cur
            if cur == target:
                ans.append(combo[:])
            if cur > target:
                return
            if len(combo) >= l:
                return

            for i in range(first_sum, l):
                if i > first_sum and candidates[i] == candidates[i-1]:
                    continue
                cur += candidates[i]
                combo.append(candidates[i])
                backtrack(i+1, combo)
                cur -= candidates[i]
                combo.pop()
            

        backtrack(0, [])
        return ans
        