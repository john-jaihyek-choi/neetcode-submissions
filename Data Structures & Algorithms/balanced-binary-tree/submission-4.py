# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Brutforce:
    # compare longest height of l and longest right of r
        # if the difference > 1, return False
# Pseudocode:
    # helper check height function:
        # base case:
            # if not root:
                # return 0
        # recursion:
            # traverse left:
                # left = dfs(root.left)
            # traverse right:
                # right = dfs(root.right)
            # return max(left, right) + 1
    # main function:
        # recurse on left
            # l_max
        # recurse on right
            # r_max
        # if abs(l_max - r_max) > 1:
            # return False
        # else:
            # return True

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        l_height = self.check_height(root.left)
        r_height = self.check_height(root.right)

        if abs(l_height - r_height) > 1:
            return False
        
        l_balanced = self.isBalanced(root.left)
        r_balanced = self.isBalanced(root.right)

        return l_balanced and r_balanced
        
    def check_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = self.check_height(root.left)
        right = self.check_height(root.right)

        return max(left, right) + 1

                
