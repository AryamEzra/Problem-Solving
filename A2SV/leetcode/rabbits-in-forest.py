class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = Counter(answers)
        print(ans)
        res = 0
        for k, v in ans.items():
            if k == 0:
                res += v
            elif v <= k + 1:
                res += (k + 1)
            else:
                res += (k+1) * ceil(v /(k+1))
        return res
            
        