class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): # O(1)
            return ""
        
        substring_char_map, t_char_map = dict(), dict()

        for c in t: # O(n)
            t_char_map[c] = t_char_map.get(c, 0) + 1

        window_match_count, t_count = 0, len(t_char_map)
        res, shortest_substring_len = [-1, -1], float("infinity")

        l = 0
        for r in range(len(s)): # O(n)
            substring_char_map[s[r]] = substring_char_map.get(s[r], 0) + 1 # O(1)
            
            if s[r] in t_char_map and substring_char_map[s[r]] == t_char_map[s[r]]: # O(1)
                window_match_count += 1 # O(1)

            while window_match_count == t_count: # O(1)
                if r - l + 1 < shortest_substring_len:
                    shortest_substring_len = r - l + 1 # O(1)
                    res = [l, r] # O(1)
                
                substring_char_map[s[l]] -= 1
                if s[l] in t_char_map and substring_char_map[s[l]] < t_char_map[s[l]]: # O(1)
                    window_match_count -= 1 # O(1)
                
                l += 1 # O(1)

        l, r = res
        return s[l: r + 1] if shortest_substring_len != float("infinity") else '' # O(k) where k is the size of the window but is bounded by n (k <= n)