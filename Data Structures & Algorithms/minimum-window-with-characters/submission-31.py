class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window problem
        # the window of string s will ATLEAST be length of t
        # characters in s doesn't necessarily have to be in the order that the characters appear in t

        # Questions:
            # are the input s and t ever going to be in different casing?
                # ex) s = "ABC" t = "abc"
            
        # Assuming the answer to the question above is Yes,
            # I'll have to add a standardization when comparing the two substrings

        # variables to store:
            # l and r
                # l will be the left pointer
                # r will be the right pointer
            # the l and r pointer index of the shortest substring
            # count of the each letters in t
            # count of the each letters in s that are in t

        # high-level:
            # iterate r as until all matching characters in t had been found
            # increment l until matching characters are found
            # in every iteration keep the record of the valid shortest substring
            # return the substring of the shortest l,r pair

        if len(s) < len(t):
            return ""

        s_map = defaultdict(int)
        t_map = defaultdict(int)

        shortest_substring_index = [-1, -1]

        for i in range(len(t)):
            t_map[t[i]] += 1

        window_match_count, t_count = 0, len(t_map)

        l, shortest_substring = 0, float('inf')
        for r in range(len(s)):
            s_map[s[r]] += 1

            if s[r] in t_map and s_map[s[r]] == t_map[s[r]]:
                window_match_count += 1

            while window_match_count == t_count:
                if shortest_substring > r - l + 1:
                    shortest_substring = r - l + 1
                    shortest_substring_index = [l, r]
                s_map[s[l]] -= 1

                if s[l] in t_map and s_map[s[l]] < t_map[s[l]]:
                    window_match_count -= 1

                l += 1
                

        l, r = shortest_substring_index
        return s[l:r + 1]
            
            

        
        
            