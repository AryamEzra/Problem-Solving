class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        check = set()
        for i in ranges:
            start, end = i
            for j in range(start, end+1):
                check.add(j)
        
        for i in range(left, right+1):
          if i not in check:
            return False
        return True
        
        

        
          
       