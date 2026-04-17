class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Note:
            - find where nums[i] + nums[j] == target
            - i != j
            - exactly 1 pair of match
        Pseudocode:
            - Bruteforce (nested loop):
                - TC: O(n^2) / SC: O(1)
                - 2 nested loops, i starts 0, j starts i + 1
                    - if nums[i] + nums[j] == target:
                        - return True
                - return False
            - Hashmap:
                - instantiate a hashmap to store complimentary value
                - iterate on nums
                    - comp = target - n
                    - if comp in hashmap:
                        return [min(i, hashmap[comp]), max(i, hasmap[comp])]
                    - hashmap[nums[i]] = i
        """

        visited = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in visited:
                return [min(i, visited[comp]), max(i, visited[comp])]
            visited[nums[i]] = i

        # length = len(nums)
        # for i in range(length):
        #     for j in range(i + 1, length):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


