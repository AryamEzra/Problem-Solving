class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        count = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                top = stack.pop()
                if stack:
                    h = min(height[stack[-1]], height[i]) - height[top]
                    w = i - (stack[-1] + 1)
                    count += (h * w)
            stack.append(i)
        return count        