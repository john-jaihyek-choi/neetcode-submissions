class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)
        for s in strs:
            c_count = [0] * 26
            for c in s:
                pos = ord(c) - ord('a')
                c_count[pos] += 1
            anagrams_map[tuple(c_count)].append(s)
        
        return anagrams_map.values()