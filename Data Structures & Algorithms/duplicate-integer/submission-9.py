class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Note:
            - Input: List[int]
            - Output: bool
            - Goal: If any value appears more than once, return true, else false
        Pseudocode:
            - Bruteforce (TC: O(n^2) / SC: O(1)):
                - 2 nested loops - i starting 0, j starting i + 1
                - if match, return true
                - else false
            - Use hashmap (TC: O(n) / SC: O(n)):
                - instantiate a set
                - iterate on nums arr
                    - if nums[i] exists in set, return true
                    - else false
        """

        visited = set()
        for n in nums:
            if n in visited:
                return True
            visited.add(n)

        return False