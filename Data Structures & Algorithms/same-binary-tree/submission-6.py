# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) -> None:
        self.t1 = []
        self.t2 = []

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        left = self.saveTreeVal(p)
        right = self.saveTreeVal(q)

        print(left)
        print(right)

        return left == right

    def saveTreeVal(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return ["None"]

        left = self.saveTreeVal(root.left)
        right = self.saveTreeVal(root.right)

        return left + right + [root.val]