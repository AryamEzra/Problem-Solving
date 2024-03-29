class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        greater = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                top = stack.pop()
                greater[top] = i - top
            stack.append(i)
        return greater
