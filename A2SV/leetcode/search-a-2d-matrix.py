class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            middle = (left+right) // 2
            r = len(matrix[0]) - 1
            l = 0
            while l <= r:
                mid = (l + r) // 2
                if matrix[middle][mid] > target:
                    r = mid - 1
                elif matrix[middle][mid] == target:
                    return True
                elif matrix[middle][mid] < target:
                    l = mid + 1
            
            if matrix[middle][mid] > target:
                right = middle - 1
            else:
                left = middle + 1
        return False
                    


        