class Solution:
    def longestPalindrome(self, s: str) -> int:
        # time: O(n)
        # space: O(n) 
        freq = {}
        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1
        print(freq)
        ans = 0
        for key, val in freq.items():
            if val % 2 == 0:
                ans += val
            if val % 2 == 1:
                ans += (val - 1)
               
        if any(val % 2 == 1 for val in freq.values()):
            ans += 1
        return ans
