class Solution:
    def reverse(self, x: int) -> int:
        maxdigit = 2147483647
        mindigit = -2147483648
        
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x:
            digit = int(x % 10)
            x = int(x / 10) 
            if (res > maxdigit // 10 or (res == maxdigit // 10 and digit >= maxdigit % 10)):
                return 0
            if (res < mindigit // 10 or (res == mindigit // 10 and digit <= mindigit % 10)):
                return 0
            
            res = (res * 10) + digit
        return sign * res
