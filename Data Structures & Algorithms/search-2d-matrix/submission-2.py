class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, columns = len(matrix), len(matrix[0]) # O(1)

        l, r = 0, rows - 1
        while l <= r: # O(log n) where n = length of the matrix array
            row = (l + r) // 2 # O(1)

            if matrix[row][0] > target: # O(1)
                r = row - 1 # O(1)
            elif matrix[row][-1] < target: # O(1)
                l = row + 1 # O(1)
            else: # O(1)
                break

        if not (l <= r):
            return False

        row = (l + r) // 2
        l, r = 0, columns - 1

        while l <= r: # O(log m) where m = length of the inner matrix array
            mid = (l + r) // 2 # O(1)

            if matrix[row][mid] > target: # O(1)
                r = mid - 1 # O(1)
            elif matrix[row][mid] < target: # O(1)
                l = mid + 1 # O(1)
            else: # O(1)
                return True # O(1)
        
        return False # O(1) 