class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #time: O(n)
        #space: O(1)

        count = [0] * 26
        req = len(s1)

        for char in s1:
            count[ord(char) - ord('a')] += 1

        l = 0
        for r in range(len(s2)):
            count[ord(s2[r]) - ord('a')] -= 1

            if count[ord(s2[r]) - ord('a')] >= 0:
                req -= 1
            while req == 0:
                if r - l + 1 == len(s1):
                    return True
                count[ord(s2[l]) - ord('a')] += 1
                if count[ord(s2[l]) - ord('a')] > 0:
                    req += 1

                l += 1
        return False



        