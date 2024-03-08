class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        r = len(citations) - 1
        c = len(citations)
        while l <= r:
            mid = (l+r) // 2
            if citations[mid] < c - mid:
                l = mid + 1
            else:
                r = mid - 1
        return c - l 
        
        