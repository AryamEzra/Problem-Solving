class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        #time: O(n)
        #space: O(1)

        skill.sort()
        ans = 0
        l = 0
        r = len(skill) - 1

        while l <= r:
            if skill[l] + skill[r] == skill[l+1] + skill[r-1]:
                ans += (skill[l] * skill[r])
                l += 1
                r -= 1
            else:
                return -1
        return ans
        