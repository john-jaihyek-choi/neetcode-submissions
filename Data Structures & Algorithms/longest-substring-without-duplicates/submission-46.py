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
            - TC: O(n^2) / SC: O(n) at worst
        Sliding Window:
            - use sliding window
            - use visited set to maintain the visited char
            - when sliding window shifts, remove left most char before shifting
            - Note:
                - no need for contracting because we only ever care about max substring length
            - Pseudocode:
                - if guard for len(s) <= 1
                - l, r = 0, 1
                - initialize visited with set(s[0])
                - while r < len(s):
                    - while s[r] in set:
                        - shift window
                - return the length of the sliding window
        """

        if len(s) <= 1: return len(s)

        l = 0
        visited = set(s[l])
        res = 0
        for r in range(1, len(s)):
            print(visited, l, r)
            while l < r and s[r] in visited:
                visited.remove(s[l])
                l+=1
            visited.add(s[r])
            res = max(res, r-l)
        return res+1
                
            

        # res = 0

        # for i, c in enumerate(s): # O(n)
        #     visited = set() # O(n) at worst
        #     for j in range(i, len(s)): # O(n)
        #         if s[j] in visited: 
        #             res = max(res, len(visited))
        #             break
        #         visited.add(s[j])
        #     else:
        #         visited.add(s[i])
        #         res = max(res, len(visited))
        
        # return res