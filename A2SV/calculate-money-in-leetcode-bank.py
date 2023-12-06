class Solution:
    def totalMoney(self, n: int) -> int:
        
        money = 0
        if n <= 7:
            for i in range(1,n+1):
                money += i
        else:
            div = n // 7
            rem = n % 7
    
            week = (28 * div) + (7 * (div * (div-1) // 2))
            
            remaining = 0
            for k in range(rem):
                remaining += (div + k + 1)
            money = week + remaining 
        return money
        
        