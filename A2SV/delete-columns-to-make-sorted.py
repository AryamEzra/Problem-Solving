class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        ''''
        for i in range(len(strs)-2):
            for j in range(len(strs[0])):
                if strs[i][j] <= strs[i+1][j] <= strs[i+2][j]:
                    count += 0
                else:
                    count += 1
        return count
        '''
        for j in range(len(strs[0])):
            for i in range(len(strs)-1):
                if strs[i][j] > strs[i+1][j]:
                    count += 1
                    break
        return count 


        
             





        