class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #time: O(n^2)
        #space: O(1)

        m = len(matrix)
        left = 0
        right = m - 1

        #reverse using a while loop
        while left < right: 
            matrix[left], matrix[right] = matrix[right], matrix[left]
            left += 1
            right -= 1
        
        #Transpose
        for i in range(m):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

