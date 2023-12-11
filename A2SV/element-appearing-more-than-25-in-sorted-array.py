class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = {}
        for count in arr:
            if count in counts:
                counts[count] += 1
            else:
                counts[count] = 1
        for key, val in counts.items():
            if val > (len(arr) // 4):
                return key
        