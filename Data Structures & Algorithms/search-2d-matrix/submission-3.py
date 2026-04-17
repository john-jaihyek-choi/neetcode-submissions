class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outer_l, outer_r = 0, len(matrix) - 1

        while outer_l <= outer_r:
            row = (outer_l + outer_r) // 2

            if matrix[row][0] <= target <= matrix[row][-1]:
                l, r = 0, len(matrix[row]) - 1

                while l <= r:
                    col = (l + r) // 2

                    if matrix[row][col] < target:
                        l = col + 1
                    elif matrix[row][col] > target:
                        r = col - 1
                    else:
                        return True

                return False

            elif matrix[row][0] > target:
                outer_r = row - 1
            elif matrix[row][-1] < target:
                outer_l = row + 1
            else:
                return True

        return False