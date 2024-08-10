# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        m = 0
        def getHeight(root):
            if root is None:
                return 0
            return 1 + max(getHeight(root.left), getHeight(root.right))
        m = getHeight(root)
        n = 2**m - 1
        res = [['' for __ in range(n)] for _ in range(m)]

        res[0][(n - 1) // 2] = str(root.val)
        def build(root, r, c):
            if root:
                res[r][c] = str(root.val)
                build(root.left, r + 1, c - 2**(m - 1 - r - 1))
                build(root.right, r + 1, c + 2**(m - 1 - r - 1))
        build(root, 0, (n - 1) // 2)
        return res