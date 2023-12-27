class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        #time: O(n)
        #space: O(1)

        right = 0
        ans = 0
        for idx, key in enumerate(flips):
            right = max(right, key)
            if right == idx + 1:
                ans += 1
        return ans

        