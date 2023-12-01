class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        enemies = {"I": ["V","X"], "X": ["L","C"], "C": ["D","M"]}
        res = 0

        for i in range(len(s)):
            if i < len(s)-1 and s[i] in enemies and s[i+1] in enemies[s[i]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]

            
        return res

        