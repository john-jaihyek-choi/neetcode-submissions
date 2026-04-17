class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t:
            return s

        shortest_substring_len = len(s) + 1
        shortest_substring = ""

        # Create a frequency map for string t
        t_map = dict()
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1

        def contains_all_chars(substring_map):
            for char, count in t_map.items():
                if substring_map.get(char, 0) < count:
                    return False
            return True
        
        # Outer loop for the left index of the window
        for l in range(len(s)):
            substring_map = dict()

            # Only process if s[l] is part of t
            if s[l] in t:
                substring_map[s[l]] = 1  # Initialize with the first character

            # Check if a single character matches the entire t
            if contains_all_chars(substring_map):
                return s[l:l + 1]  # If it's a single character that satisfies t

            # Inner loop for the right index of the window
            for r in range(l + 1, len(s)):
                if s[r] in t:
                    substring_map[s[r]] = substring_map.get(s[r], 0) + 1

                # Check if current substring contains all chars of t
                if contains_all_chars(substring_map):
                    # Update the shortest substring if a smaller one is found
                    if (r - l + 1) < shortest_substring_len:
                        shortest_substring_len = r - l + 1
                        shortest_substring = s[l:r + 1]

                    # Break early since we found a valid substring
                    break

        return shortest_substring