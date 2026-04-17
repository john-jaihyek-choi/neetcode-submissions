# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS:
        # if not root:
        #     return 0

        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)

        # return max(left, right) + 1
            
        # # Iterative DFS:
        # if not root:
        #     return 0

        stack = [[root, 0]]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
                
            if node:
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])
            
            max_depth = max(max_depth, depth)


        return max_depth
