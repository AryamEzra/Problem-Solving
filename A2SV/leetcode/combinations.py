class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # ans = []
        # nums = [i for i in range(1, n+1)]
        # def backtrack(i, combo):
        #     if len(combo) == k:
        #         ans.append(combo[:])
        #         return 
        #     if i >= n:
        #         return 
        #     backtrack(i+1, combo)
        #     combo.append(nums[i])
        #     backtrack(i+1, combo)
        #     combo.pop()
        # backtrack(0, [])
        # return ans

        ans = []
        def backtrack(first_num, path):
            if len(path) == k:
                ans.append(path[:])
                return 
            for num in range(first_num, n+1):
                path.append(num)
                backtrack(num+1, path)
                path.pop()
        backtrack(1, [])
        return ans


