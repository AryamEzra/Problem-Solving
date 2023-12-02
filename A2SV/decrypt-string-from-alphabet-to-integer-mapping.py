class Solution:
    def freqAlphabets(self, s: str) -> str:
        num = ["1", "2", "3", "4" , "5", "6", "7", "8", "9", "10#", "11#", "12#", "13#" , "14#", "15#", "16#", "17#", "18#", "19#", "20#", "21#", "22#", "23#", "24#", "25#","26#"]
        ans = []
        i = 0
        while i < len(s):
            if i+2 < len(s) and s[i+2] == "#":
                num = int(s[i:i+2])
                ans.append(chr(ord("a") + num - 1))
                i += 3
            else:
                num = int(s[i])
                ans.append(chr(ord("a") + num - 1))
                i += 1
        return "".join(ans)
        
        