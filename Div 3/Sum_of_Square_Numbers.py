class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sq = int(sqrt(c))
        
        for a in range(sq+1):
            b = sqrt(c - (a*a))
            if b == int(b): return True
        return False
        
        #time complexity: o(n +y) where y is hte time complsity of b = sqrt(c - (a*a)) and o(n) is for the for loop
        


        '''
        #Brute force approach
        a = 0
        while a*a <= c:
            b = 0
            while b*b <= c:
                if a*a + b*b == c:
                    return True
                b += 1
            a += 1
        return False
        
        '''
        
    
      
