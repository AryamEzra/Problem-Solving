class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        #time: O(n)
        #space:O(1)

        i = 0
        j = 0

        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        
        return True if i == len(name)  else False
            

        