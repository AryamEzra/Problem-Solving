class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #time: O(n)
        #space: O(1)

        vowels = {"a", "e", "i", "o", "u"}
        count = 0
        res = 0

        left = 0
        for right in range(len(s)):
            if s[right] in vowels:
                count += 1
            if right - left + 1 > k:
                #after shifting the window if the char we just removed was a vowel we want to decrement our count before shifting our left pointer
                if s[left] in vowels:
                    count -= 1
                left += 1
            
            res = max(res, count)
        return res
        
            
                

        