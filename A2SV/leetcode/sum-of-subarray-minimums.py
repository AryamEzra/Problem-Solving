class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # to find the next smaller greater element -> use a montonically incresing stack
        stack = []
        a = len(arr)
        prev_smaller = [-1] * a
        next_smaller = [a] * a

        ans = 0
        for idx, num in enumerate(arr):
            while stack and arr[stack[-1]] > arr[idx]:
                top = stack.pop()
                next_smaller[top] = idx
            if stack:
                prev_smaller[idx] = stack[-1]
            stack.append(idx)
        
        for idx, num in enumerate(arr):
            ans += num * (idx - prev_smaller[idx]) * (next_smaller[idx] - idx)
            ans %= (10 ** 9 +  7)
        return ans 


        



        