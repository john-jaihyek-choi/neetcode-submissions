class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False       

class PrefixTree:
    """
    1. initialize PrefixTree
        - initializes root for the prefix tree
    2. insert
        - iterate on word:
            - create new TrieNode if no children by "char" exists
            - traverse the head to the children TrieNode
        - update the end indicator
    3. search
        - iterate on word:
            - if char doesn't exist in children of the node traversing
                - return False
        - if at the end of the iteration, the node.end is True:
            - return True
        - else
            - return false
    4. startswith
        - iterate on word:
            if char doesn't exist in children of the node traversing
                return False
        - return True if iteration completes without exiting
    """

    def __init__(self):
        # SC: O(t) where t is all nodes in root
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # TC: O(n) where n is len(word)
        head = self.root

        for char in word:
            char_pos = ord(char) - ord("a")
            if not head.children[char_pos]:
                head.children[char_pos] = TrieNode()

            head = head.children[char_pos]

        head.end = True

    def search(self, word: str) -> bool:
        # TC: O(n) where n is len(word)
        head = self.root

        for char in word:
            char_pos = ord(char) - ord("a")
            if not head.children[char_pos]:
                return False

            head = head.children[char_pos]

        return head.end

    def startsWith(self, prefix: str) -> bool:
        # TC: O(n) where n is len(word)
        head = self.root

        for char in prefix:
            char_pos = ord(char) - ord("a")
            if not head.children[char_pos]:
                return False

            head = head.children[char_pos]

        return True