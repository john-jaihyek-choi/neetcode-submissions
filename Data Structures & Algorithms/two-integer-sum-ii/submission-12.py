class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Pseudocode:
        # Two pointer approach:
            # instantiate a left and right pointer, l and r
                # l begins from 0
                # r begins from len(numbers) - 1
            # while l is less than r:
                # if numbers[l] + numbers[r] < target:
                    # l += 1
                # elif numbers[l] + numbers[r] > target:
                    # r -= 1
                # elseL:
                    # return [l + 1, r + 1]
            # return []
            
        l, r = 0, len(numbers) - 1

        while l < r:
            sum_val = numbers[l] + numbers[r]
            if sum_val < target:
                l += 1
            elif sum_val > target:
                r -= 1
            else:
                return [l + 1, r + 1]
            
        return []