class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        space_set = set(spaces)
        for index, char in enumerate(s):
            if index in space_set:
                ans.append(" ")
            ans.append(char)
        return "".join(ans)
                
            

        