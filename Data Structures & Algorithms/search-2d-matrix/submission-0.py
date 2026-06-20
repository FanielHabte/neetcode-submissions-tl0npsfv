class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left, right= 0, len(matrix) -1
        while left <= right:
            mid = (left + right) // 2

            mid_matrix = matrix[mid]

            if mid_matrix[0] <= target <= mid_matrix[-1]:
                return target in mid_matrix
            
            if mid_matrix[-1] >= target:
                right = mid - 1
            if mid_matrix[-1] <= target:
                left = mid + 1
            
        return False