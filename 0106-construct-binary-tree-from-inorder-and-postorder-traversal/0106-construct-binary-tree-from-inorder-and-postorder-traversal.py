# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        index = {}
        for i in range(n):
            index[inorder[i]] = i

        def build(a, b, c, d):
            ''' 
                `a` and `b` represent subarray [a...b] of inorder list
                and `c` and `d` represent subarray [c...d] of postorder list

             '''

            if a == b:
                return TreeNode(inorder[a])
            if a > b:
                return None

            ix = index[postorder[d]]
            node = TreeNode(postorder[d])
            leftSize = ix - a

            node.left = build(a, ix - 1, c, c + leftSize - 1)
            node.right = build(ix + 1, b, c + leftSize, d - 1)

            return node

        return build(0, n - 1, 0, n - 1)