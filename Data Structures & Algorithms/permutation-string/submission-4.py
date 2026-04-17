class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        
        # If s1 is longer than s2, return False
        if m > n:
            return False
        
        # Frequency arrays for s1 and for the current window in s2
        s1_count = [0] * 26  # Frequency array for s1
        s2_count = [0] * 26  # Frequency array for the sliding window in s2
        
        # Fill the frequency array for s1
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
        
        # Initialize the first window in s2
        for i in range(m):
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        # Compare the first window
        if s1_count == s2_count:
            return True
        
        # Start sliding the window
        for i in range(m, n):
            s2_count[ord(s2[i]) - ord('a')] += 1
            s2_count[ord(s2[i - m]) - ord('a')] -= 1
            
            if s1_count == s2_count:
                return True
        
        # If no permutation found
        return False