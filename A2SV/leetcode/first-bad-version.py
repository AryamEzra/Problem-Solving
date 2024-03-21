# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        # ans was previusly n 
        while l <= r:
            mid = l + (r-l) // 2
            if isBadVersion(mid): # return True -  bad
                # ans = mid
                r = mid - 1
            else: # return false - not bad
                l = mid + 1
        return l
        