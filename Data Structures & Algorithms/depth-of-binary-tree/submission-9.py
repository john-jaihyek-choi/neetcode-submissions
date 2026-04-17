# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS:
        # Pseudocode:
            # base case:
                # if root is not valid:
                    # return 0
            # traverse the left of the tree
                # left = maxDepth(root.left) + 1
            # traverse the right of the tree
                # right = maxDepth(root.right) + 1
            # return max(left, right)

        # TC: O(n) / SC: O(h) h for the height of the tree for the callstack
        if not root:
            return 0

        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1

        return max(left, right)

        # Iterative DFS - use own stack:
        # Pseudocode:
            # set empty stack with an initial item of [root, depth] pair
                # root = root
                # depth = 0
            # while stack is non-empty:
                # pop the stack and retrieve the root and the depth
                # if node is non empty:
                    # append the left and the right node to the stack
                        # right first, then left
                        # compute the new depth when appending to stack
                # compute the max_depth 
            # return the max_depth
        
        stack = [[root, 0]]
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            if node:
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])
                max_depth = max(max_depth, depth)
        
        return max_depth




            

