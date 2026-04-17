# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursive DFS:
        # if not root:
        #     return None

        # temp = root.left
        # root.left = root.right
        # root.right = temp

        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)
            
        # return root

        # iterative DFS:
        # if not root:
        #     return root

        # stack = [root]
        
        # while stack:
        #     node = stack.pop()
        #     node.left, node.right = node.right, node.left
        #     if node.left:
        #         stack.append(node.left)
            
        #     if node.right:
        #         stack.append(node.right)

        # return root

        # iterative BFS:
        if not root:
            return root

        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return root

