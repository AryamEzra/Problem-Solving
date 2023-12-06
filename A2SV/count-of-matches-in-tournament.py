class Solution:
    def numberOfMatches(self, n: int) -> int:
        output = 0
        while n != 1:
            ans = n / 2
            floor_ans = floor(ans)
            ans = ceil(ans)
            output += floor_ans
            n = ans
        
        return output

       
        