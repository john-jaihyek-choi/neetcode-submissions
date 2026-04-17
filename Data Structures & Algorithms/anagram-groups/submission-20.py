class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Note:
            - group words that are anagrams of each other in an array of arrays
                - res[i] = group
                - res[i][j] = word in a group
        Brainstorm:
            - Bruteforce:
                - Create a hashmap of sorted words
                    ex) {
                        "act": ["act", "cat"]
                    }
                - iterate on strs arr, sort the word, and add to hashmap if it doesn't already exist
                - iterate on strs array
            - Better Solution:
                -  26 letters at max
                - Use array hashing with hashmap (visited)
                - iterate on w
                    - count instances of each character and register in an array (len(arr) = 26)
                    - check if the unique arr exists:
                        - if true, append to the visited[w]
                        - else, add 
        """

        # visited = defaultdict(list)
        # for w in strs:
        #     hashed_w = [0] * 26
        #     for c in w:
        #         hashed_w[ord(c) - ord("a")] += 1
        #     visited[tuple(hashed_w)].append(w)

        # return list(visited.values())
            

        # TC: O(n) * O(k log k) / SC: O(n * k)
        visited = defaultdict(list)
        for w in strs:
            sorted_w = "".join(sorted(w))
            if sorted_w in visited:
                visited[sorted_w].append(w)
                continue
            visited[sorted_w] = [w]

        return list(visited.values())
        