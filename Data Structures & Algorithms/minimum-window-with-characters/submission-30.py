class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return "" 

        t_count = defaultdict(int)
        window_count = defaultdict(int)
        
        for c in t:
            t_count[c] += 1

        shortest_substring_length = float('inf')
        shortest_substring_pair = [-1, -1]

        have, need = 0, len(t_count)


        l = 0
        for r in range(len(s)):
            window_count[s[r]] += 1

            if s[r] in t_count and window_count[s[r]] == t_count[s[r]]:
                have += 1

            while have >= need:
                if r - l + 1 < shortest_substring_length:
                    shortest_substring_length = r - l + 1
                    shortest_substring_pair = [l, r]

                window_count[s[l]] -= 1

                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1

                l += 1

        l, r = shortest_substring_pair
        return s[l:r + 1] if shortest_substring_length != float("inf") else ""
            
                