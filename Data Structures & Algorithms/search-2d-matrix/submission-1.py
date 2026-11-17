class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix) - 1
        col = l

        # find the correct col
        while l <= r:
            mid = (l + r) // 2

            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                col = mid
                break

        l = 0
        r = len(matrix[col]) - 1

        while l <= r:
            mid = (l + r) // 2

            if target > matrix[col][mid]:
                l = mid + 1
            elif target < matrix[col][mid]:
                r = mid - 1
            else:
                return True
    
        return False