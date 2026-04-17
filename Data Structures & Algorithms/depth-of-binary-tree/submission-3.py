# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive DFS:
        # base case:
            # if root is None:
                # return 0
        # else:
            # set left depth
            # set right depth
            # return bigger of the two depths

        # TC: O(n) / SC: O(n)
        # if not root:
        #     return 0
        
        # left = self.maxDepth(root.left) + 1
        # right = self.maxDepth(root.right) + 1

        # return max(left, right)

        # Iterative BFS:
        # use deque to keep track of left and right nodes in the tree
        if not root:
            return 0
        
        layer = 0
        q = deque([root])
        while q:
            
            # take snapshot of q len, then iterate len(q) many times to pop items for given layer (breadth)
            for _ in range(len(q)):
                # node will contain popped node
                node = q.popleft()
                # check if popped node have left value
                if node.left:
                    q.append(node.left)
                # check if popped node have right value
                if node.right:
                    q.append(node.right)

            # when done with layer iteration, increase layer
            layer += 1
        
        return layer
        
        # Iterative DFS:
        # use of stack per layer

        # if not root:
        #     return 0

        # layer = 0
        # stack = list([root])

        # while stack:

        #     for _ in range(len(stack)):
        #         node = stack.pop()
        #         if node.right:
        #             stack.append(node.right)
        #         if node.left:
        #             stack.append(node.left)
                
        #     layer += 1
        
        # return layer


