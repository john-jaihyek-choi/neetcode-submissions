class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Note:
            - Goal: numbers[index1] + numbers[index2] == target
            - Must be O(1) SC
        Brute force:
            - 2 loops - i, j where j is i + 1
            - iterate numbers
                - if numbers[i] + numbers[j] == target
                    - return its values pair
            - TC: O(n^2) / SC: O(1)
        Two-Pointer:
            - l, r start at each end
            - if numbers[l] + numbers[r] > target
                - move smaller of l/r
            - if numbers[l] + numbers[r] < target
                - move bigger of the l/r
        """

        # for i in range(0, len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]
        
        # return []

        l, r = 0, len(numbers)-1
        while l < r:
            sum_val = numbers[l] + numbers[r]
            if sum_val > target:
                r -= 1
            elif sum_val < target:
                l += 1
            else:
                return [l+1, r+1]

        return []
            
            