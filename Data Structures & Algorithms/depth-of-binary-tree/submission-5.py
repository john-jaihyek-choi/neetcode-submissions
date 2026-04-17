# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive DFS:
        # if not root:
        #     return 0

        # left = self.maxDepth(root.left)
        # right = self.maxDepth(root.right)

        # max_depth = max(left, right) + 1

        # return max_depth

        # iterative DFS:
        if not root:
            return 0

        max_depth = 0
        stack = [[root, 1]]
        
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])
                
        return max_depth

        # iterative BFS:
        if not root:
            return 0

        q = deque([root])
        max_depth = 0

        while q:
            node = q.popleft()

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            max_depth += 1

        return max_depth
            
            

            

