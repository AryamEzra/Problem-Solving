class Solution:
    def pow(self, x: int, y: int, mod: int) -> int:

            if y == 0:
                return 1
            if y == 1:
                return x

            val = self.pow(x, y // 2, mod)

            if y % 2 == 0:
                return (val * val) % mod
            else:
                return (x * val * val) % mod

    def countGoodNumbers(self, n: int) -> int:
        ans = 1
        exp = n // 2
        mod = 10**9 + 7

        
        if n % 2 == 0:            
            ans = (self.pow(5, exp, mod) * self.pow(4, exp, mod))
        
        else:
            ans = (self.pow(5, exp, mod) * 5 * self.pow(4, exp, mod))
    
        return ans % mod


        
        





        
        
        
        
            
        