"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        dp = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = grid[i][j] + dp[i + 1][j] + dp[i][j + 1] - dp[i + 1][j + 1]
        
        def makeQuadTree(row1, col1, row2, col2):
            if row1 > row2 or col1 > col2:
                return None
            size = (row2 - row1 + 1) * (col2 - col1 + 1)
            numOnes = dp[row1][col1] - dp[row2 + 1][col1] - dp[row1][col2 + 1] + dp[row2 + 1][col2 + 1]
            if numOnes == 0:
                return Node(0, True)
            elif numOnes == size:
                return Node(1, True)
            else:
                topLeft = makeQuadTree(row1, col1, (row1 + row2) // 2, (col1 + col2) // 2)
                topRight = makeQuadTree(row1, (col1 + col2) // 2 + 1, (row1 + row2) // 2, col2)
                bottomLeft = makeQuadTree((row1 + row2) // 2 + 1, col1, row2, (col1 + col2) // 2)
                bottomRight = makeQuadTree((row1 + row2) // 2 + 1, (col1 + col2) // 2 + 1, row2, col2)
                return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
                
        return makeQuadTree(0, 0, n - 1, n - 1)