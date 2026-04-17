# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) -> None:
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Pseudocode:
            # General idea:
                # recurse the tree, then compare the depth and the diameter at each recursion state
            # base case:
                # if root is None:
                    # return 0
            # recurse:
                # recurse left 
                # recurse right
            # compute the longer of the two:
                # diameter
                # depth
            # return max_diameter
        self.dfs(root)

        return self.max_diameter

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        height = max(left, right)
        self.max_diameter = max(self.max_diameter, left + right)

        return height + 1