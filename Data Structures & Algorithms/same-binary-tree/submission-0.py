# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # input:
            # p: TreeNode || None
                # root of the first tree
            # q: TreeNode || None
                # root of the second tree
        # goal:
            # return boolean:
                # True if p and q are same
                # False otherwise
            # trees are "same" if the values and the order of the nodes are the same.
        # Brainstorm:
            # Bruteforce Idea:
                # iterate on root1 and and root2, then collect the nodes in 2 set of arrays
                # compare the 2 arrays if identical
            
        # Pseudocode (Bruteforce):
            # Create a separate method that traverses and copies the node.val to the array (dfs)
                # input:
                    # root: TreeNode | None
                # output:
                    # List[int | None]
                # base case:
                    # if not root:
                        # return []
                    # traverse left node
                        # left = self.dfs(root.left)
                    # traverse right node
                        # right = self.dfs(root.right)
                    # return left + right + [root.val]
            # from the isSameTree method, call the dfs method on root1 and root2:
                # return self.dfs(p) == self.dfs(q)

        return self.dfs(p) == self.dfs(q)
    
    def dfs(self, root: Optional[TreeNode]) -> List[int | None]:
        if not root:
            return ['Null']
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        return left + right + [root.val]
