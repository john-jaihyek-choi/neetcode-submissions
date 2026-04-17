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
        """

        for i in range(0, len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
        
        return []
            