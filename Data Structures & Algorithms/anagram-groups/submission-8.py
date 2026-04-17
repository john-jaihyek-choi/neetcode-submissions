class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_arr = []
        anagram_group = {}

        for word in strs:
            char_count = {}
            for char in word:
                char_count[char] = 1 + char_count.get(char, 0)

            print(f'char_count: {char_count}')
            hashed_count = hash(str(sorted(char_count.items())))

            if hashed_count in anagram_group:
                anagram_group[hashed_count].append(word)
            else:
                anagram_group[hashed_count] = [word]

        for group in anagram_group:
            res_arr.append(anagram_group[group])

        return res_arr