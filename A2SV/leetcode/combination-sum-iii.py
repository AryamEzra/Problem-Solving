class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        cur = 0
        def backtrack(i, combo):
            nonlocal cur
            if cur == n and len(combo) == k :
                ans.append(combo[:])
            if i >= n:
                return
            if cur > n:
                return 
            if len(combo) == k:
                return
            if i >= 1 and i <= 9:
                cur += i
                combo.append(i)
                backtrack(i+1, combo)
                cur -= i
                combo.pop()
                backtrack(i+1, combo)
        backtrack(1, [])
        return ans

