class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # time complexity: O(n*m)
        # space somplexity: 0(1)
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        
        '''
        # time complexity: O(n*m)
        # space somplexity: 0(n)
        ans = []
        for i in range(len(matrix[0])):
            res = []
            for j in range(len(matrix)):
                res.append(matrix[j][i])
            ans.append(res)
        return ans
        '''