class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): # O(1)
            return ""
        
        substring_char_map, t_char_map = dict(), dict()
        window_match_count, t_count = 0, len(t)
        res, shortest_substring_len = [-1, -1], float("infinity")

        for c in t: # O(n)
            t_char_map[c] = t_char_map.get(c, 0) + 1
            substring_char_map[c] = 0

        l = 0
        for r in range(len(s)): # O(n)
            if s[r] in t_char_map: # O(1)
                substring_char_map[s[r]] += 1 # O(1)
                window_match_count += 1 # O(1)

            while window_match_count >= t_count and self.matching_characters(t_char_map, substring_char_map): # O(m)
                shortest_substring_len = min(shortest_substring_len, r - l + 1) # O(1)
                res = [l, r] # O(1)
                
                if s[l] in t_char_map: # O(1)
                    substring_char_map[s[l]] -= 1 # O(1)
                    window_match_count -= 1 # O(1)

                l += 1 # O(1)

        l, r = res
        return s[l: r + 1] if shortest_substring_len != float("infinity") else '' # O(k) where k is the size of the window but is bounded by n (k <= n)

    def matching_characters(self, t_char_map, substring_char_map):
        for c, count in t_char_map.items(): # O(m) where m = len(t) - duplicate character
            if substring_char_map.get(c, 0) < count:
                return False
            
        return True