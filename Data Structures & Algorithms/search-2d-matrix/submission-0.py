class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outer_l, outer_r = 0, len(matrix) - 1

        while outer_l <= outer_r:
            outer_mid = (outer_l + outer_r) // 2

            if matrix[outer_mid][0] <= target <= matrix[outer_mid][-1]:
                inner_l, inner_r = 0, len(matrix[outer_mid]) - 1

                while inner_l <= inner_r:
                    inner_mid = (inner_l + inner_r) // 2

                    if matrix[outer_mid][inner_mid] > target:
                        inner_r = inner_mid - 1
                    elif matrix[outer_mid][inner_mid] < target:
                        inner_l = inner_mid + 1
                    else:
                        return True
                
                return False

            elif matrix[outer_mid][0] > target:
                outer_r = outer_mid - 1
            elif matrix[outer_mid][0] < target:
                outer_l = outer_mid + 1
            else:
                return True
        
        return False        