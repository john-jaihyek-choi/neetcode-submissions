class Solution:
    def minWindow(self, s: str, t: str) -> str:
        output = ''
        if len(s) < len(t):
            return output
        
        substring_char_map, t_char_map = dict(), dict()
        shortest_substring_len = len(s)
        window_match_count, t_count = 0, len(t)

        for c in t:
            t_char_map[c] = t_char_map.get(c, 0) + 1
            substring_char_map[c] = 0

        l = 0
        for r in range(len(s)):
            if t_char_map.get(s[r]):
                substring_char_map[s[r]] += 1
                window_match_count += 1

            while window_match_count >= t_count and self.matching_characters(t_char_map, substring_char_map):
                shortest_substring_len = min(shortest_substring_len, r - l + 1)
                output = s[l:l + shortest_substring_len]
                
                if s[l] in t_char_map:
                    substring_char_map[s[l]] -= 1
                    window_match_count -= 1

                l += 1

        return output

    def matching_characters(self, t_char_map, substring_char_map):
        for c, count in t_char_map.items():
            if substring_char_map.get(c, 0) < count:
                return False
            
        return True