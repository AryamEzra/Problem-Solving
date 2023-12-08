class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = "0"
        for i in range(len(num)):
            if int(num[i]) % 2 == 1:
                odd=(num[:i+1])
                
        return "" if odd == "0" else odd
        