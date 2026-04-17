# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Pseudocode:
            # base case:
                # if root is not valid:
                    # return 0
            # traverse the left of the tree
                # left = maxDepth(root.left) + 1
            # traverse the right of the tree
                # right = maxDepth(root.right) + 1
            # return max(left, right)

        if not root:
            return 0

        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return max(left, right)

            

            

