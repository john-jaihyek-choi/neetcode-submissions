# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# input:
    # p: TreeNode
    # q: TreeNode
# output:
    # output: bool
        # True if p and q are identical
        # False otherwise
# goal:
    # given root of 2 trees, return true if two trees are same and False otherwise

# Brainstorm:
    # Bruteforce solution?
        # traverse the p and q separately, then store the nodes to an array in the same order
        # compare the arrays and return the result
        # TC: O(n + m) / SC: O(n + m)

# Pseudocode (Bruteforce):
    # initialize 2 arrays to store p nodes and q nodes separately
    # traverse the p tree
        # recursively set node.val to the p_array
    # traverse the q tree
        # recursively set node.val to the q_array
# Bruteforce:
class Solution:
    def __init__(self) -> None:
        self.p_arr = []
        self.q_arr = []
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        self.dfs_tree(p, self.p_arr)
        self.dfs_tree(q, self.q_arr)

        print('p_nodes', self.p_arr)
        print('q_nodes', self.q_arr)
        return self.p_arr == self.q_arr
        
    def dfs_tree(self, root: Optional[TreeNode], node_storage: List[int]) -> None:
        if not root:
            node_storage.append('None')
            return None

        left = self.dfs_tree(root.left, node_storage)
        right = self.dfs_tree(root.right, node_storage)

        node_storage.append(root.val)