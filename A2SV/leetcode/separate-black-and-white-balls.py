class Solution:
    def minimumSteps(self, s: str) -> int:
        #time:
        #space:
        i = 0
        j = len(s) - 1
        ans = 0
        while i < j:
            if s[i] == "0":
                i += 1
            elif s[j] == "1":
                j -= 1
            else:
                ans += (j-i)
                i += 1
                j -= 1

        return ans