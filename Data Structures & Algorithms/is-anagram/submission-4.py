class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Note:
            Anagram:
                - exact same characters
                - same number of characters
                - order can differ
            Constraint:
                - s and t are both lower case
        Pseudocode:
            - Bruteforce (sorting):
                - TC: O(nlogn) / SC: O(s) + O(t) = O(n)
                - sort s and t
                - if s == t, true
                - else false
            - Hashmap
                - if len(s) != len(t)
                    - return False
                - instantiate hashmap for s_map and t_map
                - iterate s
                    - if s[i] in s_map:
                        - s[i] + 1
                    - else:
                        - s[i] = 0
                - iterate t
                    - if t[i] in t_map:
                        - t[i] + 1
                    - else:
                        - t[i] = 0
                - iterate on s_map.entries() (l = letter, c= count):
                    if t_map[l] != c:
                        - return False
                    return True
        """
        
        s_map, t_map = {}, {}
        for c in s:
            if c in s_map:
                s_map[c] += 1
            else:
                s_map[c] = 0

        for c in t:
            if c in t_map:
                t_map[c] += 1
            else:
                t_map[c] = 0

        return s_map == t_map


        print(s_map)




        # sorted_s, sorted_t = sorted(s), sorted(t)
        # if sorted_s == sorted_t:
        #     return True
        # return False