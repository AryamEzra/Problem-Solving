class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in {"+", "-", "*", "/"}:
                stack.append(int(c))
            else:
                if stack and c == "+":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = val1 + val2
                    stack.append(res)
                    
                elif stack and c == "*":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = val1 * val2
                    stack.append(res)

                elif stack and c == "-":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = val2 - val1
                    stack.append(res)

                elif stack and c == "/":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    res = int(val2 / val1)
                    stack.append(res)
                    
        return stack[-1]
            

                    
        
        
        