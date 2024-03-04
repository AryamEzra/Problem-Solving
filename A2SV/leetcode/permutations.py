class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(path):
            if len(path) == n:
                ans.append(path[:])
                return
            for i in range(n):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(path)
                path.pop()
        backtrack([])
        return ans

        