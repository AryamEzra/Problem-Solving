class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count = 0
        stack = [0]
        
        for i in s:
            if i == "(":
                stack.append(0)
            elif stack:
                val1 = stack.pop()
                val2 = stack.pop()
                tmp = val2 + max(2*val1, 1)
                stack.append(tmp)

        return stack[-1]

        
        