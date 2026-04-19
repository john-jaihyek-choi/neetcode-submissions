class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Note:
            - ouput: length of the longest substring
            - s == ASCII chars
        Bruteforce:
            - 2 loops
                - maintain "visited" count
                - add each s[j] to visited
                - if already exists, record the length
            - TC: O(n^2) / SC: O(n)
        """

        res = 0

        for i, c in enumerate(s):
            visited = set()
            for j in range(i, len(s)):
                if s[j] in visited:
                    res = max(res, len(visited))
                    break
                visited.add(s[j])
            else:
                visited.add(s[i])
                res = max(res, len(visited))
        
        return res