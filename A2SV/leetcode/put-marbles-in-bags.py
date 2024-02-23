class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        cost = 0
        split = []
        left = 0
        right = 0
        for i in range(len(weights)-1):
            split.append(weights[i] + weights[i+1])
        split.sort()
        for i in range(k-1):
            left += split[i]
        split.sort(reverse = True)
        for i in range(k-1):
            right += split[i]

        return right - left
        

                





        