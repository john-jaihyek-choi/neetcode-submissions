# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # note:
            # In order for a tree to be balanced:
                # the difference between the left and the right height must be no greater than 1
        # Brainstorm:
            # what is needed?
                # the height at left and right is needed
            # what do I need to process?
                # get the bigger of the left or the right height and return to its parent (with +1)
                # This gives the total max left and max right heights
            # compute the difference of the left and the right height
        if not root:
            return True

        res = self.height_dfs(root)

        return res[1]

    def height_dfs(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return [0, True]
        
        left_h, left_isBalanced = self.height_dfs(root.left)
        right_h, right_isBalanced = self.height_dfs(root.right)

        height = max(left_h, right_h)
        isBalanced = abs(left_h - right_h) <= 1 and left_isBalanced and right_isBalanced

        return [height + 1, isBalanced]
