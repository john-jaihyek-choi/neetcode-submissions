# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Note:
            - for each node, switch left with right
                - dfs to left
                - dfs to right
            - dfs function:
                - base case: node is None
        """

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return node

            node.left, node.right = node.right, node.left

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return root