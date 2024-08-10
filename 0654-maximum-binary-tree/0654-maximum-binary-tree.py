# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def build(i, j):
            if j - i < 0:
                return None
            elif j - i == 0:
                return TreeNode(nums[i])
            else:
                largestIndex = i
                for ix in range(i + 1, j + 1):
                    if nums[ix] > nums[largestIndex]:
                        largestIndex = ix
                root = TreeNode(nums[largestIndex])
                root.left = build(i, largestIndex - 1)
                root.right = build(largestIndex + 1, j)
                return root
        return build(0, len(nums) - 1)