class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #time: O(n)
        #space: O(1)

        ptr1 = 0
        ptr2 = 0
        g1 = len(g)
        s1 = len(s)
        g.sort()
        s.sort()
        happy  = 0
        while ptr1 < g1 and ptr2 < s1:
            if s[ptr2] >= g[ptr1]:
                happy += 1
                ptr1 += 1
            ptr2 += 1
        return happy


