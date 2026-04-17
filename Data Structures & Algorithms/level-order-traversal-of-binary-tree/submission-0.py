# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Note:
            - Level order traversal
                - top to bottom, left to right
        Intuition:
            - use BFS:
                - traverse from the root node:
                    - use q to store each level of a tree
                    - append each node in the q's left and right nodes
        """
        output = []
        if root is None:
            return output

        q = deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()

                if node:
                    level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            output.append(level)
            
        return output