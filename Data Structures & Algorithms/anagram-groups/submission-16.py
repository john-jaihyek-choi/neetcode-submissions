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
        """

        visited = defaultdict(list)
        for w in strs:
            sorted_w = "".join(sorted(w))
            if sorted_w in visited:
                visited[sorted_w].append(w)
                continue
            visited[sorted_w] = [w]

        return list(visited.values())
        