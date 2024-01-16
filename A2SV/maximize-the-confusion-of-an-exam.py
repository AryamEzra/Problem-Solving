class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        #time: O(n)
        #space: o(n)

        count = {}
        res = 0

        left = 0
        for right in range(len(answerKey)):
            count[answerKey[right]] = 1 + count.get(answerKey[right], 0)
            while (right - left + 1) - max(count.values()) > k:
                count [answerKey[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res
        
        