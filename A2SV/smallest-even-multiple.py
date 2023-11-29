class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        sml = 0
        if n % 2 != 0:
            sml = n * 2
        else:
            sml = n
        return sml
        
        