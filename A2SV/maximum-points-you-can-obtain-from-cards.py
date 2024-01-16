class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #time: O(n)
        #space: O(1)

        r = len(cardPoints) - k
        total = sum(cardPoints[r:])
        res = total
        l = 0
        while r < len(cardPoints):
            total += cardPoints[l] - cardPoints[r]
            res = max(total, res)
            l += 1
            r += 1
        return res


        