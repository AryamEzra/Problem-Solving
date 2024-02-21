class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        #the max number of 10's we can see is 11
        ans = Counter(answers)
        res = 0
        for k, v in ans.items():
            if k == 0:
                res += v
            elif v <= k + 1:
                res += (k + 1)
            else:
                res += (k+1) * ceil(v /(k+1))
        return res
            
        