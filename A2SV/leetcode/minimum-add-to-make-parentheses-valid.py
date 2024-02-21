class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        stack = []
        for i in range(len(s)):

            if s[i] == "(":
                stack.append(s[i])
            elif (len(stack) != 0) and s[i] == ")":
                stack.pop()
            elif (len(stack) == 0) and s[i] == ")":
                count += 1  
        
        return count + len(stack)
        