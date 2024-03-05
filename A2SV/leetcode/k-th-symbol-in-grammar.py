class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def solve(n,k):
            if n == 1:
                return 0
            p = solve(n-1, ceil(k/2))
            
            if p == 0 and k % 2 == 0:
                return 1
            if p == 0 and k % 2 == 1:
                return 0
            if p == 1 and k % 2 == 0:
                return 0
            if p == 1 and k % 2 == 1:
                return 1
            

        
        return solve(n, k)





        