# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Note:
            # height-balanced: left height - right height <= 1
            # recursive condition:
                # check left height and right height difference at each node
                    # if abs(l_height - r_height) > 1:
                        # return False
                    # else
                        # return True
        isBalanced, _ = self.heightBalanced(root)

        return isBalanced

    def heightBalanced(self, root: Optional[TreeNode]) -> List[bool | int]:
        if not root:
            return [True, 0]
        
        l_bal, l_h = self.heightBalanced(root.left)
        r_bal, r_h = self.heightBalanced(root.right)

        if abs(l_h - r_h) > 1 or not l_bal or not r_bal:
            return [False, 0]

        return [True, max(l_h, r_h) + 1]

        

        
