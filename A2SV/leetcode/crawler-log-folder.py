class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for i in logs:
            if i == "./":
                continue
            if stack and i == "../":
                stack.pop()

            if i != "../":
                stack.append(i)

        return len(stack)
        