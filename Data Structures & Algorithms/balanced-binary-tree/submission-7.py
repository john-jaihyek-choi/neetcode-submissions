# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Brutforce (TC: O(n^2) / SC: O(h)):
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
        # recurse on left and get max l height
            # l_max
        # recurse on right and get max r height
            # r_max
        # if abs(l_max - r_max) > 1:
            # return False
        # else:
            # recurse the main funcion passing left node
                # l_balanced = main(node.left)
            # recurse the main funcion passing left node
                # r_balanced = main(node.right)
        # return l_balanced and r_balanced

# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True

#         l_height = self.check_height(root.left)
#         r_height = self.check_height(root.right)

#         if abs(l_height - r_height) > 1:
#             return False
        
#         l_balanced = self.isBalanced(root.left)
#         r_balanced = self.isBalanced(root.right)

#         return l_balanced and r_balanced
        
#     def check_height(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         left = self.check_height(root.left)
#         right = self.check_height(root.right)

#         return max(left, right) + 1

# Ideas to optimize:
    # how do I prevent checking height O(n) operation each state?
        # pass height and balance state from the top of the call stack
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        _, bal = self.check_h_and_bal(root)

        return bal
    
    def check_h_and_bal(self, root: Optional[TreeNode]) -> List[int | bool]:
        if not root:
            return [0, True]

        l_h, l_bal = self.check_h_and_bal(root.left)
        r_h, r_bal = self.check_h_and_bal(root.right)

        return [max(l_h, r_h) + 1, abs(l_h - r_h) <= 1 and l_bal and r_bal]
        

        
