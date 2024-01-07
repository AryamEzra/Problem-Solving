class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #time: O(n**2)
        #space: O(n)

        longest = 0
        substring = []
        for i in range(len(s)):
            if s[i] not in substring:
                substring.append(s[i])
                longest = max(longest, len(substring))
            else:
                index = substring.index(s[i])
                substring = substring[index + 1:] +  [s[i]]
        longest = max(longest, len(substring))
        return longest




        