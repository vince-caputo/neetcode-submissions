class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        while bottom - top >= 2:
            mid = (bottom + top) // 2
            if matrix[mid][0] >= target:
                bottom = mid
            else:
                top = mid

        at = top
        if target >= matrix[bottom][0]:
            at = bottom
        else:
            at = top
        left = 0
        right = len(matrix[0]) - 1
        while right - left >= 2:
            mid = (right + left) // 2
            if matrix[at][mid] == target:
                return True
            elif matrix[at][mid] < target:
                left = mid
            else:
                right = mid
        return matrix[at][left] == target or matrix[at][right] == target
        










