class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        n = len(nums)
        nums.sort()
        def backtrack(i, combo):
            if i >= n:
                visited.add(tuple(combo[:]))
                return 
            backtrack(i+1, combo)
            combo.append(nums[i])
            backtrack(i+1, combo)
            combo.pop()
        backtrack(0, [])
            
        return list(visited)