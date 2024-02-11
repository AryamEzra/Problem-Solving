class Solution:
    def balancedString(self, s: str) -> int:
        #time: O(n)
        #space: O(n)

        freq = {"Q":0, "E":0, "W":0, "R":0,}
        l = len(s)
        for i in range(l):
            freq[s[i]] += 1
        # print(freq)
        target = l // 4
        min_replace = l
        left = 0
        for right in range(l):
            freq[s[right]] -= 1
            while (left < l and freq["Q"] <= target and freq["E"] <= target and freq["R"] <= target and freq["W"] <= target):
                min_replace = min(min_replace, right - left + 1)
                freq[s[left]] += 1
                left += 1

        return min_replace