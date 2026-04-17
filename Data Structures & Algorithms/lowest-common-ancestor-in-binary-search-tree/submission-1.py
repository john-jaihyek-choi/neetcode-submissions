# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Note:
            - Binary Search Tree!!!
                - left smaller
                - right bigger
            - conditions:
                - if p == root:
                    - p is LCA
                - if q == root:
                    - q is LCA
                - elif p < root and q > root or p > root and q < root:
                    - root is LCA
                - elif p < root and q < root:
                    - traverse to the left
                - elif p > root and q > root:
                    - traverse to the left
        Intuition:
            - compare p and q value at each node
        """

        node = root
        
        while node:
            if p.val == node.val or q.val == node.val:
                return p if p.val == node.val else q
            if (p.val < node.val and q.val > node.val) or (p.val > node.val and q.val < node.val):
                return node

            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right

        return node