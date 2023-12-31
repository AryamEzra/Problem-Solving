class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        #time:O(nlogn)
        #space:O(1)

        piles.sort()
        n = len(piles)
        step = n // 3

        total = 0
        for i in range(n-2, step-1, -2):
            total += piles[i]
        return total
        