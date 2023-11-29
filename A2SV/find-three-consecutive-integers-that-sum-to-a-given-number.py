class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans = []
        x2 = num // 3
        x3 = x2 + 1
        x1 = x2 - 1
        total = x1 + x2 + x3
        if num == total:
            return[x1, x2, x3]
        else:
            return []

