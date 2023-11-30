class Solution:
    def interpret(self, command: str) -> str:
        ans = []
        for i in range(len(command)):
            if command[i] == "G":
                ans.append(command[i])
            elif command[i] == "(" and command[i+1] == ")":
                ans.append("o")
            elif command[i] == "(" and command[i+1] == "a" and command[i+2] == "l" and command[i+3] == ")" :
                ans.append("al")
            
        return "".join(ans)
            
        