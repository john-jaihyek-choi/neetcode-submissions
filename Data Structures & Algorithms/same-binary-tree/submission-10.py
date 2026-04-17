# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        left = self.sameTree(p.left, q.left)
        right = self.sameTree(p.right, q.right)

        return left and right and p.val == q.val
        
    def sameTree(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False

        left = self.sameTree(node1.left, node2.left)
        right = self.sameTree(node1.right, node2.right)

        return left and right