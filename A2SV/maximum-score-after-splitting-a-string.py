class Solution:
    def maxScore(self, s: str) -> int:
        #time: O(n)
        #space: O(1)

        zero = 0
        one = s.count("1")
        res = 0

        x = len(s)
        for i in range(x-1):
            if s[i] == "0":
                zero += 1
            else:
                one -= 1
            res = max(res, zero + one)
        return res 

    
        