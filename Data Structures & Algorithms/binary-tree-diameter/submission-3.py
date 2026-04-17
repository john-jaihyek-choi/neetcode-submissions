# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Note:
            - DFS
                - traverse to all left and right nodes
                - max depth is the sum of max left depth and max right depth
        """

        # DFS
        if root is None:
            return 0

        diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            nonlocal diameter
            left = dfs(node.left)
            right = dfs(node.right)
            
            diameter = max(left + right, diameter)

            return max(left, right) + 1

        dfs(root)

        return diameter
