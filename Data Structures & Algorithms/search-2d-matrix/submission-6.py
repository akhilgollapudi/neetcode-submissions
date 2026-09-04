class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_start = []
        for i in range(len(matrix)):
            row_start.append(matrix[i][0])
        left = 0
        right = len(row_start) - 1
        row = 0
        while left <= right:
            mid = (left + right) // 2
            if target >= row_start[mid]:
                left = mid + 1
            else:
                right = mid - 1
        row = right
        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            if target > matrix[row][mid]:
                left = mid + 1
            if target < matrix[row][mid]:
                right = mid - 1
        return False