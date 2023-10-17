class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [-1 for _ in range(n)]
        for u in range(n):
            for v in (leftChild[u], rightChild[u]):
                if v == -1:
                    continue
                if parent[v] != -1:
                    return False
                parent[v] = u
        
        active = [False for _ in range(n)]
        seen = [0 for _ in range(n)]
        def existCycle(u):
            active[u] = True
            for v in (leftChild[u], rightChild[u]):
                if v == -1:
                    continue
                if active[v]:
                    return True
                seen[v] = 1
                cycle = existCycle(v)
                if cycle:
                    return True
            active[u] = False
            return False
        
        root = -1
        for i in range(n):
            if parent[i] == -1:
                if root != -1:
                    return False
                root = i
        seen[root] = 1

        if existCycle(root):
            return False
        
        return sum(seen) == n        