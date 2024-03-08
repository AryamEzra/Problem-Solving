class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        l = 0
        r = 1
        t =  len(s)
        lst = [char for char in s]
        seen = set(s)
        ans = ""
        for i in range(t):
            if s[i].swapcase() in seen:
                ans += s[i]
            else: 
                var1 = "".join(lst[:i])
                var2 = "".join(lst[i+1:])
                left = self.longestNiceSubstring(var1)
                right = self.longestNiceSubstring(var2)
                return max(left, right, key=len)

        return ans

        