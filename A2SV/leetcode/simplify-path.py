class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = ["/"]
        for i in path:
            if i == "" or i == ".":
                continue
            if stack and i == ".." and len(stack) > 1:
                stack.pop()
                stack.pop()

            if i != "..":
                stack.append(i)
                stack.append("/")

        if stack[-1] == "/" and len(stack) > 1:
            stack.pop()

        return "".join(stack)
        