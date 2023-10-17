class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        self.components = 0
        def dfs(u, p):
            for v in adj[u]:
                if v != p:
                    values[u] += dfs(v, u)
            
            if not values[u] % k:
                self.components += 1
                return 0
            else:
                return values[u]
                
        dfs(0, -1)
        return self.components
