class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {char: index for index, char in enumerate(s)}
        ans = []
        start, end = 0, 0

        for i, char in enumerate(s):
            last_index = dic[char]  
            end = max(end, last_index)  
            
            if i == end:  
                ans.append(i - start + 1)
                start = i + 1  

        return ans
        
                

            